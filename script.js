function addTask() {
    var taskInput = document.getElementById("taskInput");
    var taskList = document.getElementById("taskList");

    if (taskInput.value === "") {
        alert("Please enter a task.");
        return;
    }

    var newTask = document.createElement("li");
    var taskText = document.createElement("span");
    taskText.innerText = taskInput.value;
    newTask.appendChild(taskText);

    taskText.addEventListener("click", toggleTask);

    taskList.appendChild(newTask);

    taskInput.value = "";
}

function toggleTask() {
    this.classList.toggle("completed");
}

// Press Enter key to add task
var input = document.getElementById("taskInput");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        addTask();
    }
});

