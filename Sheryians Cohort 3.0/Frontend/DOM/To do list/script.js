let addBtn = document.querySelector("#add_btn");
let editBtn = document.querySelector("#edit_btn");
let deleteBtn = document.querySelector("#delete_btn");
let addInput = document.querySelector("#add_input")
let tasks = document.querySelector(".tasks")
addBtn.addEventListener("click", function(){
    if(addInput.value!==""){
        const task = document.createElement("div");
        task.classList.add("task")
        task.innerHTML = `<div class="task-p1">
                            <p>${addInput.value}</p>
                        </div>
                        <div class="task-p2">
                            <div class="edit">
                                <button id="edit_btn">Edit</button>
                            </div>
                            <div class="delete">
                                <button id="delete_btn">Delete</button>
                            </div>
                        </div>`
        tasks.prepend(task);
    }
    addInput.value="";
});

editBtn.addEventListener("click", function(){
    console.log("edit");
});

deleteBtn.addEventListener("click", function(){
    console.log("delete");
});

