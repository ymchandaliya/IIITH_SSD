function checkforp(){
    console.log(1);
    p = document.getElementById("pass");
    cp = document.getElementById("cfp");
    if(p.value!=cp.value){
        alert("please check your password");
        cp.value = "";
    }
}

function checkUname(){
    uname = document.getElementById("uname").value;
    x = document.getElementById("error");
    u = /[A-Z]/.test(uname);
    d = /[0-9]/.test(uname);
    console.log(u);
    console.log(d);
    if(u == false || d == false){
        x.innerHTML = "invalid username";
    
    }
    else{
        x.innerHTML = "";
    }
}

function allowit(evtdrag){
    evtdrag.preventDefault();
}

function drag(evtdrag){
    evtdrag.dataTransfer.setData("DraggedId", evtdrag.target.id);    
}

function dropit(evtdrag){
        evtdrag.preventDefault();

        eId = evtdrag.dataTransfer.getData("DraggedId");
        evtdrag.target.appendChild(document.getElementById(eId));
}

function showData(){
    m = document.getElementById("mngr").value;
    e = document.getElementById("email").value;
    u = document.getElementById("uname").value;
    t = document.getElementById("tl").value;
    let litems = document.getElementById("div9").getElementsByTagName("li");
    console.log(litems);
    s = "";
    for(let i = 0; i <= litems.length - 1; i++)
        s += litems[i];
    alert('name: ' + m + '\nemail: ' + e + '\nUsername: ' + u + '\nTeam Lead: ' + t + '\n' + s);
}