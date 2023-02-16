alert("You are opening the ToDo List")

window.addEventListener('load', () => {
    const form = document.querySelector("#osnova-form");
    const input = document.querySelector("#osnova-input");
    let list_el = document.querySelector(".task-list");;





    form.addEventListener('submit', (e) =>{
        e.preventDefault();
        const task = input.value;
        if (!task){
            alert("Enter your task");
            return;
        }
        list_el.classList.add("task-list-style");
        const task_el = document.createElement("div");
        task_el.classList.add("task");
        const task_content_el = document.createElement("div");
        task_content_el.classList.add("content");
        const task_check_el = document.createElement("input");
        task_check_el.type = "checkbox";
        const task_input_el = document.createElement("input");
        task_input_el.classList.add("text");
        task_input_el.type = "text";
        task_input_el.value = task;
        task_input_el.setAttribute("readonly", "readonly");

        task_content_el.appendChild(task_input_el);

        const task_action_el = document.createElement("div");
        task_action_el.classList.add("actions");
        const task_delete_el = document.createElement("button");
        task_delete_el.classList.add("delete");
        task_delete_el.innerHTML = "<img src=\"delete.png\" style=\"width: 25px\">";
        task_action_el.appendChild(task_delete_el);
        

        task_el.appendChild(task_check_el);
        task_el.appendChild(task_content_el);
        task_el.appendChild(task_action_el);

        input.value = "";

        task_check_el.addEventListener('change', () =>{
            if(task_check_el.checked){
                task_input_el.classList.add("lineThrough");
            } else{
                task_input_el.classList.remove("lineThrough");
            }
        });


        task_delete_el.addEventListener('click', () =>{
            list_el.removeChild(task_el);
        });


        list_el.appendChild(task_el);
        console.log(list_el);
    });
});