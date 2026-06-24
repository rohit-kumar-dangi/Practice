const taskForm = document.querySelector("#taskForm");
const taskInput = document.querySelector("#taskInput");
const categoryInput = document.querySelector("#categoryInput");
const taskList = document.querySelector("#taskList");

const searchInput = document.querySelector("#searchInput");
const filterCategory = document.querySelector("#filterCategory");

const themeToggle = document.querySelector("#themeToggle");
const clearAllBtn = document.querySelector("#clearAllBtn");

const totalCount = document.querySelector("#totalCount");
const completedCount = document.querySelector("#completedCount");
const pendingCount = document.querySelector("#pendingCount");
const emptyMessage = document.querySelector("#emptyMessage");

let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

/*
  ATTRIBUTE VS PROPERTY DEMO

  taskInput.value:
  Gives current value typed by the user.

  taskInput.getAttribute("value"):
  Gives original value written in HTML.

  Example:
  If HTML has <input value="Initial task">

  taskInput.value can change when user types.
  taskInput.getAttribute("value") remains "Initial task".
*/

console.log("Property value:", taskInput.value);
console.log("Attribute value:", taskInput.getAttribute("value"));

function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function updateCounters() {
  const total = tasks.length;

  const completed = tasks.filter(function (task) {
    return task.status === "completed";
  }).length;

  const pending = tasks.filter(function (task) {
    return task.status === "pending";
  }).length;

  totalCount.textContent = total;
  completedCount.textContent = completed;
  pendingCount.textContent = pending;

  if (tasks.length === 0) {
    emptyMessage.classList.remove("hidden");
  } else {
    emptyMessage.classList.add("hidden");
  }
}

function createTaskCard(task) {
  const taskCard = document.createElement("article");

  taskCard.classList.add("task-card");

  if (task.status === "completed") {
    taskCard.classList.add("completed");
  }

  // Required custom attributes
  taskCard.setAttribute("data-id", task.id);
  taskCard.setAttribute("data-status", task.status);
  taskCard.setAttribute("data-category", task.category);

  // dataset usage
  taskCard.dataset.id = task.id;
  taskCard.dataset.status = task.status;
  taskCard.dataset.category = task.category;

  const taskInfo = document.createElement("div");
  taskInfo.classList.add("task-info");

  const title = document.createElement("h3");
  title.classList.add("task-title");

  // createTextNode() required by assignment
  const titleText = document.createTextNode(task.title);
  title.append(titleText);

  const categoryBadge = document.createElement("span");
  categoryBadge.classList.add("category-badge");
  categoryBadge.textContent = task.category;

  taskInfo.append(title);
  taskInfo.append(categoryBadge);

  const taskActions = document.createElement("div");
  taskActions.classList.add("task-actions");

  const editButton = document.createElement("button");
  editButton.classList.add("task-action-btn", "edit-btn");
  editButton.textContent = "Edit";

  const completeButton = document.createElement("button");
  completeButton.classList.add("task-action-btn", "complete-btn");

  completeButton.textContent =
    task.status === "completed" ? "Undo" : "Complete";

  const deleteButton = document.createElement("button");
  deleteButton.classList.add("task-action-btn", "delete-btn");
  deleteButton.textContent = "Delete";

  taskActions.append(editButton, completeButton, deleteButton);

  taskCard.append(taskInfo, taskActions);

  return taskCard;
}

function renderTasks() {
  taskList.innerHTML = "";

  const fragment = document.createDocumentFragment();

  const searchText = searchInput.value.toLowerCase().trim();
  const selectedCategory = filterCategory.value;

  const filteredTasks = tasks.filter(function (task) {
    const matchesSearch = task.title.toLowerCase().includes(searchText);

    const matchesCategory =
      selectedCategory === "All" || task.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  filteredTasks.forEach(function (task) {
    const taskCard = createTaskCard(task);
    fragment.append(taskCard);
  });

  taskList.append(fragment);

  updateCounters();
}

taskForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const title = taskInput.value.trim();
  const category = categoryInput.value;

  if (title === "") {
    alert("Please enter a task title.");
    return;
  }

  const newTask = {
    id: Date.now().toString(),
    title: title,
    category: category,
    status: "pending"
  };

  tasks.unshift(newTask);

  saveTasks();
  renderTasks();

  taskInput.value = "";
  taskInput.focus();
});

/*
  EVENT DELEGATION

  One listener is attached to taskList.
  It handles Edit, Complete, and Delete buttons
  even for newly created task cards.
*/
taskList.addEventListener("click", function (event) {
  const button = event.target.closest("button");

  if (!button) return;

  const taskCard = button.closest(".task-card");

  if (!taskCard) return;

  const taskId = taskCard.dataset.id;

  const taskIndex = tasks.findIndex(function (task) {
    return task.id === taskId;
  });

  if (taskIndex === -1) return;

  if (button.classList.contains("delete-btn")) {
    // remove() required by assignment
    taskCard.remove();

    tasks.splice(taskIndex, 1);

    saveTasks();
    renderTasks();
  }

  if (button.classList.contains("complete-btn")) {
    const currentStatus = taskCard.dataset.status;

    if (currentStatus === "pending") {
      tasks[taskIndex].status = "completed";
      taskCard.dataset.status = "completed";
      taskCard.setAttribute("data-status", "completed");
    } else {
      tasks[taskIndex].status = "pending";
      taskCard.dataset.status = "pending";
      taskCard.setAttribute("data-status", "pending");
    }

    saveTasks();
    renderTasks();
  }

  if (button.classList.contains("edit-btn")) {
    const oldTitle = tasks[taskIndex].title;

    const updatedTitle = prompt("Edit your task:", oldTitle);

    if (updatedTitle && updatedTitle.trim() !== "") {
      tasks[taskIndex].title = updatedTitle.trim();

      saveTasks();
      renderTasks();
    }
  }
});

searchInput.addEventListener("input", function () {
  renderTasks();
});

filterCategory.addEventListener("change", function () {
  renderTasks();
});

clearAllBtn.addEventListener("click", function () {
  if (tasks.length === 0) {
    alert("There are no tasks to clear.");
    return;
  }

  const shouldClear = confirm("Are you sure you want to delete all tasks?");

  if (shouldClear) {
    tasks = [];
    saveTasks();
    renderTasks();
  }
});

/*
  THEME TOGGLE
  Uses classList, dataset, and setAttribute()
*/
themeToggle.addEventListener("click", function () {
  document.body.classList.toggle("dark-mode");

  if (document.body.classList.contains("dark-mode")) {
    document.body.dataset.theme = "dark";
    document.body.setAttribute("data-theme", "dark");
    themeToggle.textContent = "☀️ Light Mode";
  } else {
    document.body.dataset.theme = "light";
    document.body.setAttribute("data-theme", "light");
    themeToggle.textContent = "🌙 Dark Mode";
  }

  localStorage.setItem("theme", document.body.dataset.theme);
});

function loadTheme() {
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    document.body.dataset.theme = "dark";
    themeToggle.textContent = "☀️ Light Mode";
  }
}

/*
  Required methods demonstration:
  append(), prepend(), before(), after(), replaceWith(), remove()

  These examples are only for learning.
  They are commented so they do not change your real UI.
*/

/*
const demoElement = document.createElement("p");
demoElement.textContent = "DOM Method Demo";

taskList.append(demoElement);
taskList.prepend(demoElement);

taskList.before(demoElement);
taskList.after(demoElement);

const replacement = document.createElement("p");
replacement.textContent = "Replacement Element";

demoElement.replaceWith(replacement);

replacement.remove();
*/

/*
  Required attribute methods demonstration
*/

/*
const firstTask = document.querySelector(".task-card");

if (firstTask) {
  console.log(firstTask.getAttribute("data-id"));

  firstTask.setAttribute("data-example", "hello");

  console.log(firstTask.hasAttribute("data-example"));

  firstTask.removeAttribute("data-example");
}
*/

/*
  EVENT PROPAGATION DEMO
*/

const grandparent = document.querySelector("#grandparent");
const parent = document.querySelector("#parent");
const childButton = document.querySelector("#childButton");

// Capturing phase: top to bottom
grandparent.addEventListener(
  "click",
  function () {
    console.log("Grandparent - Capturing");
  },
  true
);

parent.addEventListener(
  "click",
  function () {
    console.log("Parent - Capturing");
  },
  true
);

childButton.addEventListener(
  "click",
  function () {
    console.log("Child - Capturing");
  },
  true
);

// Bubbling phase: bottom to top
childButton.addEventListener("click", function () {
  console.log("Child - Bubbling");
});

parent.addEventListener("click", function () {
  console.log("Parent - Bubbling");
});

grandparent.addEventListener("click", function () {
  console.log("Grandparent - Bubbling");
});

loadTheme();
renderTasks();