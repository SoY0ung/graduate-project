from PIL import Image
import cmd2
import getpass
import os
import subprocess
import matplotlib.pyplot as plt

from faceutil import FaceUtil

database_path = 'database/'
faceutil = None
threshold = 1.10

class FaceManagementMenu(cmd2.Cmd):
    """人脸管理 二级菜单"""
    prompt = "(face-admin) "
    intro = "输入 ? 或 help 获取命令列表。"

    def __init__(self):
        super().__init__()
        # 添加命令别名
        shortcuts = dict(cmd2.DEFAULT_SHORTCUTS)
        shortcuts.update({'？':'help', 'exit': '返回exit',
                          'add': '添加人脸add', 'update': '更新人脸update',
                          'remove': '删除人脸remove',})
        cmd2.Cmd.__init__(self, shortcuts=shortcuts)


    @cmd2.with_category("人脸管理")
    def do_添加人脸add(self, arg):
        print('请选择添加方式（输入数字）：')
        opt = int(input('[1] 从相机中添加\n[2] 从文件中添加\n'))
        face = None
        if opt == 1:
            print("提示：即将打开相机，取景框左上角倒计时结束后会自动拍照")
            os.system('pause')
            face = faceutil.get_cam_faces()
            if len(face) > 0:
                face = face[0]
            else:
                print("未检测到人脸!")
                return
        elif opt == 2:
            print("请选择包含人脸的图片进行添加...")
            path = image_picker_win()
            face = Image.open(path)
            face = faceutil.get_img_faces(face)
            if len(face) > 0:
                face = face[0]
            else:
                print("未检测到人脸!")
                return
        if face is not None:
            name = input('请输入人脸名称：')
            if faceutil.add_face(face, name):
                print('成功添加人脸：'+name)
            else:
                print('人脸名称已存在！')
        # 实现添加人脸数据的逻辑

    @cmd2.with_category("人脸管理")     
    def do_更新人脸update(self, arg):
        names = faceutil.list_face()
        print('系统中已有的人脸名称：')
        print(names, sep=',')
        name = input('请输入要更新的人脸名称：')
        if name not in names:
            print('人脸名称不存在！')
            return
        print('请选择更新方式（输入数字）：')
        opt = int(input('[1] 从相机中更新\n[2] 从文件中更新\n'))
        face = None
        if opt == 1:
            print("提示：即将打开相机，取景框左上角倒计时结束后会自动拍照")
            os.system('pause')
            face = faceutil.get_cam_faces()
            if len(face) > 0:
                face = face[0]
            else:
                print("未检测到人脸!")
                return
        elif opt == 2:
            print("请选择包含人脸的图片进行更新...")
            path = image_picker_win()
            face = Image.open(path)
            face = faceutil.get_img_faces(face)
            if len(face) > 0:
                face = face[0]
            else:
                print("未检测到人脸!")
                return
        if face is not None:
            name = input('请输入人脸名称：')
            if faceutil.update_face(face, name):
                print('成功添加人脸：'+name)
            else:
                print('人脸名称不存在！')
        # 实现添加人脸数据的逻辑

    @cmd2.with_category("人脸管理")
    def do_删除人脸remove(self, arg):
        names = faceutil.list_face()
        print('系统中已有的人脸名称：')
        print(names, sep=',')
        name = input('请输入要删除的人脸名称：')
        if name not in names:
            print('人脸名称不存在！')
            return
        if faceutil.remove_face(name):
            print('成功删除人脸：'+name)
        else:
            print('人脸名称不存在！')
    
    @cmd2.with_category("人脸管理")
    def do_返回exit(self, arg):
        """返回上一层菜单"""
        return super().do_quit(arg)

class FaceRecognitionCLI(cmd2.Cmd):
    """
    人脸识别比对系统 命令行主界面
    """
    prompt = "(user) "
    intro = "欢迎使用人脸识别系统！输入 ? 或 help 获取命令列表。"

    def __init__(self):
        super().__init__()
        # 创建人脸管理二级菜单
        self.face_management_menu = FaceManagementMenu()

        # 添加命令别名
        shortcuts = dict(cmd2.DEFAULT_SHORTCUTS)
        shortcuts.update({'？':'help', 'su': '管理员登录su', 'exit':'退出管理员模式exit',
                          'cam':'打开相机cam', 'pic':'选择图片pic', 'face':'人脸管理face',
                          'pwd':'修改管理员密码pwd'})
        cmd2.Cmd.__init__(self, shortcuts=shortcuts)


        # 默认用户态
        self.admin_mode = False
        self.admin_password = "123456"  # 管理员密码

    @cmd2.with_category("人脸比对系统")
    def do_打开相机cam(self, arg):
        """打开相机进行人脸比对。"""
        print("提示：即将打开相机，取景框左上角倒计时结束后会自动拍照")
        os.system('pause')

        camface = faceutil.get_cam_faces()
        if len(camface) > 0:
            camface = camface[0]
        else:
            print("未检测到人脸!")
            return
        # plt.imshow(camface)
        # plt.show()
        name, dist = faceutil.recognize_face(camface)
        if dist>threshold:
            print("未找到匹配的人脸！", name, dist)
        else:
            print(f"你好，{name}", dist)

    @cmd2.with_category("人脸比对系统")
    def do_选择图片pic(self, arg):
        """选择图片进行人脸比对。"""
        print("请选择图片进行人脸比对...")
        path = image_picker_win()
        # print(path)
        img = Image.open(path)
        img = faceutil.get_img_faces(img)
        if len(img) > 0:
            img = img[0]
        else:
            print("未检测到人脸！")
            return
        # plt.imshow(img)
        # plt.show()
        name, dist = faceutil.recognize_face(img)
        if dist>threshold:
            print("未找到匹配的人脸！", name, dist)
        else:
            print(f"你好，{name}", dist)

    @cmd2.with_category("管理员")
    def do_管理员登录su(self, arg):
        """输入管理员密码进入管理态。"""
        password_input = getpass.getpass('请输入管理员密码: ')
        if password_input == self.admin_password:
            self.admin_mode = True
            self.prompt = "(admin) "
            print("已进入管理态。")
        else:
            print("密码错误。")

    @cmd2.with_category("管理员")
    def do_退出管理员模式exit(self, arg):
        """退出管理模式，返回用户模式。"""
        self.admin_mode = False
        self.prompt = "(user) "
        print("已退出管理态。输入quit来退出程序")

    # 管理态专用命令
    @cmd2.with_category("管理员")
    def do_人脸管理face(self, arg):
        """进入人脸管理菜单。"""
        if self.admin_mode:
            self.face_management_menu.cmdloop()
        else:
            print("此操作需要管理员权限。")

    @cmd2.with_category("管理员")
    def do_修改管理员密码pwd(self, arg):
        """修改管理员密码。"""
        if self.admin_mode:
            new_password = getpass.getpass('请输入新的管理员密码: ')
            self.admin_password = new_password
            print("管理员密码已成功修改。")
        else:
            print("此操作需要管理员权限。")

def image_picker_win():
    PS_Commands = "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8;"
    PS_Commands += "Add-Type -AssemblyName System.Windows.Forms;"
    PS_Commands += "$fileBrowser = New-Object System.Windows.Forms.OpenFileDialog;"
    PS_Commands += '$fileBrowser.Title = "请选择图片";'
    PS_Commands += '$fileBrowser.Filter = "JPEG files (*.jpg)|*.jpg";'
    PS_Commands += "$Null = $fileBrowser.ShowDialog();"
    PS_Commands += "echo $fileBrowser.FileName"
    file_path = subprocess.run(["powershell.exe", PS_Commands], stdout=subprocess.PIPE)
    file_path = file_path.stdout.decode()
    file_path = file_path.rstrip()
    return file_path


if __name__ == '__main__':
    faceutil = FaceUtil(database_path=database_path)
    app = FaceRecognitionCLI()
    app.cmdloop()
