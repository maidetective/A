import os
import shutil


def file_op():
    if os.path.exists("./批量操作"):
        shutil.rmtree("./批量操作")
    os.mkdir("./批量操作")
    os.chdir("./批量操作")
    for i in range(1, 21):
        file = open(f"lala{i}.py", "w", encoding="utf-8")
        file.write('eval("print(\'hellow,world\')")')
        file.close()


def file_ch():
    print(os.getcwd())
    cd = "F:\\learn\\python\\day7begin\\批量操作"
    if os.getcwd() != cd:
        os.chmod(cd)
    file_list_name = os.listdir()
    print(file_list_name)
    for name in file_list_name:
        os.rename(name, f"python{name}")


file_op()
file_ch()
