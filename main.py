from PIL import Image
from calc_face import face_distance

import cmd2
import getpass

class FaceManagementMenu(cmd2.Cmd):
    """人脸管理 二级菜单"""
    prompt = "(face-admin) "
    intro = "输入 ? 或 help 获取命令列表。"

    def __init__(self):
        super().__init__()
        # 添加命令别名
        shortcuts = dict(cmd2.DEFAULT_SHORTCUTS)
        shortcuts.update({'？':'help', 'exit': '返回',
                          'add': '添加人脸add', 'update': '更新人脸update',
                          'modify': '修改人脸modify', 'remove': '删除人脸remove',})
        cmd2.Cmd.__init__(self, shortcuts=shortcuts)


    @cmd2.with_category("人脸管理")
    def do_添加人脸add(self, arg):
        """添加新的人脸数据。"""
        print("添加新的人脸数据...")
        # 实现添加人脸数据的逻辑

    @cmd2.with_category("人脸管理")     
    def do_更新人脸update(self, arg):
        """更新现有的人脸数据。"""
        print("更新现有的人脸数据...")
        # 实现更新人脸数据的逻辑

    @cmd2.with_category("人脸管理")
    def do_修改人脸modify(self, arg):
        """修改现有的人脸数据。"""
        print("修改现有的人脸数据...")
        # 实现修改人脸数据的逻辑

    @cmd2.with_category("人脸管理")
    def do_删除人脸remove(self, arg):
        """删除人脸数据。"""
        print("正在删除人脸数据...")
        # 实现删除人脸数据的逻辑
    
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
        print("正在打开相机进行人脸比对...")
        # 在这里实现具体的人脸比对逻辑
        print("人脸比对完成。欢迎您！")

    @cmd2.with_category("人脸比对系统")
    def do_选择图片pic(self, arg):
        """选择图片进行人脸比对。"""
        print("请选择图片进行人脸比对...")
        # 在这里实现选择图片和进行人脸比对的逻辑
        print("人脸比对完成。欢迎您！")

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


if __name__ == '__main__':
    app = FaceRecognitionCLI()
    app.cmdloop()
