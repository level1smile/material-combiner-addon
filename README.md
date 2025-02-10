由DeepSeek 进行汉化代码编写，以下为原版说明的汉化内容：
===========
#### 2025 02 10 


material-combiner-addon
===========
#### 这是一个用于 Blender 的插件，旨在帮助减少游戏引擎中的绘制调用，通过合并纹理而不损失质量，并避免 UV 边界超出 0-1 范围的问题。

#### 如果你喜欢这个插件，可以在 Patreon 上支持我的工作，或者请我喝杯咖啡。
[<img src="http://webgrimes.com/buymeacoffee.svg" height="40px">](https://www.buymeacoffee.com/shotariya)
[<img src="http://webgrimes.com/patreon.png" height="40px">](https://www.patreon.com/join/shotariya?)

## 功能
* **合并多个材质**：允许你将漫反射颜色与纹理混合，并指定生成的图集大小以及每个单独纹理的大小。
* **多重合并**：为每个材质添加图像层，这些层被合并到不同的图集中。此功能支持生成法线贴图、高光贴图和其他图集。（在新版本中未实现 | 在 2.0.3.3 版本中支持）
* **UV 打包**：通过分割网格面将 UV 打包到选定的比例范围内，并且兼容绑定模型。（在新版本中未实现 | 在 1.1.6.3 版本中支持）

## 安装
1. 下载插件：[Material-combiner](https://github.com/Grim-es/material-combiner-addon/archive/master.zip)。
2. 打开 Blender，进入 `文件 > 用户偏好 > 插件`。
3. 点击 `从文件安装插件`。
4. 选择 `material-combiner-addon-master.zip` 文件。
5. 启用 Material Combiner 插件。

## 使用方法
1. 插件安装并启用后，进入 Blender 的 3D 视口。
2. 在 3D 视口（场景）窗口的右侧，按下键盘上的 `N` 键打开侧边面板。
3. 在侧边面板中，找到 **MatCombiner** 部分。
4. 你会看到对象及其对应材质的列表：
   - 对于每个材质，你可以通过勾选或取消勾选旁边的框来选择是否将其包含在图集生成过程中。
   - 每个对象都有一个 **全选** 或 **取消全选** 按钮，可以快速启用或禁用其所有材质的图集生成。
5. 你还可以为没有图像的材质设置大小。默认大小为 32 像素。
6. 选择完成后，点击 `Save atlas to..` 按钮开始图集生成过程。
7. 如果材质没有正确合并或图集图像不包含所有纹理，请参考以下部分：
   [点击 "Save atlas to.." 后，材质只是简单地合并或图集图像不包含所有纹理](https://github.com/Grim-es/material-combiner-addon/tree/master?tab=readme-ov-file#after-clicking-save-atlas-to-the-materials-are-simply-merged-or-the-atlas-image-does-not-have-all-the-textures)。

## 已知问题

### 点击 "Save atlas to.." 后，材质只是简单地合并或图集图像不包含所有纹理
- 纹理被打包在 .blend 文件中。将 .blend 文件保存到你选择的位置，然后进入 `文件 > 外部数据 > 解包资源 / 解包所有到文件` 以提取纹理。
- 你使用的 Blender 版本不是英文版，在这种情况下，节点的名称会有所不同，脚本中严格规定了节点的名称。你需要手动将节点重命名为正确的名称，或者将 Blender 版本切换为英文并重新导入模型以重新生成节点。
- 你使用了不受支持的着色器（材质的表面属性）或错误的节点名称。你可以查看文件 [utils/materials.py](https://github.com/Grim-es/material-combiner-addon/blob/781d70fbbc2ddfa6813c61255c0cb6c501307a3e/utils/materials.py#L19-L40) 来了解哪些着色器受支持以及应该使用哪些节点名称。更多详细信息，请参考 GitHub 上的相关讨论：[Issue #98](https://github.com/Grim-es/material-combiner-addon/issues/98)。
- 如果对象已经共享相同的材质和纹理，它们将不会被图集化，因为它们已经优化，并且会使用现有的图像。

### Pillow 安装过程重复
- 确保 VPN 当前未启用。

- **Windows** | 确认 Blender 不是从 Windows 商店安装的，否则可能无法正常工作。要手动安装 Pillow，请导航到你的 Blender 安装文件夹，然后进入 ***blender 版本名称\python\bin*** 文件夹并复制此路径。按下键盘上的 ***Win+R***，输入 ***cmd.exe***，然后按 Enter。在 Windows 控制台中，输入以下命令：
    ```powershell
    set PythonPath="你复制的路径\到\Python\bin\文件夹"

    %PythonPath%\python.exe -m pip install Pillow --user --upgrade
    ```
    将 ***你复制的路径\到\Python\bin\文件夹*** 替换为你复制的路径。

- **MacOS** | 打开终端控制台并执行以下命令：
    ```bash
    /Applications/Blender.app/Contents/MacOS/Blender -b --python-expr "__import__('ensurepip')._bootstrap()" 

    /Applications/Blender.app/Contents/MacOS/Blender -b --python-expr "__import__('pip._internal')._internal.main(['install', '-U', 'pip', 'setuptools', 'wheel'])"

    /Applications/Blender.app/Contents/MacOS/Blender -b --python-expr "__import__('pip._internal')._internal.main(['install', 'Pillow'])"
    ```
  如果你将 Blender 安装在其他位置，请调整每个命令开头的路径。

### 没有名为 'material-combiner-addon-2' 的模块
你从 Releases 中安装了源代码。请改为从 master 分支安装 [Material-combiner](https://github.com/Grim-es/material-combiner-addon/archive/master.zip)。在安装之前，请删除旧的安装文件夹。默认位置为：
* **Windows**
    ```console
    C:\Users\你的用户名\AppData\Roaming\Blender Foundation\Blender\Blender版本\scripts\addons
    ```
  将 ***你的用户名*** 替换为你的实际用户名，将 ***Blender版本*** 替换为你使用的 Blender 版本。
* **MacOS**
    ```console
    /Users/你的用户名/Library/Application Support/Blender/Blender版本/scripts/addons
    ```
  将 ***你的用户名*** 替换为你的实际用户名，将 ***Blender版本*** 替换为你使用的 Blender 版本。

## 错误 / 建议
如果你发现了错误或有改进工具的建议，可以通过 Discord 联系我：[@shotariya](https://discordapp.com/users/275608234595713024)
