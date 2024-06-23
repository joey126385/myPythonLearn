let login = document.getElementById("login")
login.addEventListener("click", () => {
    let userName = document.getElementById("userName")
    console.log(userName);
    console.log(userName.value);

    let userPass = document.getElementById("userPass")
    console.log(userPass);
    console.log(userPass.value);

    console.log(userName.value,"---",typeof userName.value);
    if (userName.value != null) {
        console.log("ok,用户名非空");
        if (userPass.value.length == 8) {
            alert("登录成功");

        } else {
            alert("密码长度必须为8位！！");
        }
    } else {
        alert("用户不能为空")
    }
}
)

