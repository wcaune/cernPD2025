# WSL2环境下Geant4和ROOT完整安装教程

本教程详细记录在Windows Subsystem for Linux 2 (WSL2)环境中使用Miniconda安装Geant4和ROOT的完整流程，并包含B1例子的编译和运行验证。

## 目录

- [前置条件](#前置条件)
- [第一步：系统准备](#第一步系统准备)
- [第二步：安装Miniconda](#第二步安装miniconda)
- [第三步：配置Conda镜像源](#第三步配置conda镜像源)
- [第四步：创建专用环境](#第四步创建专用环境)
- [第五步：安装Geant4和ROOT](#第五步安装geant4和root)
- [第六步：验证安装](#第六步验证安装)
- [第七步：测试B1例子](#第七步测试b1例子)
- [常见问题](#常见问题)
- [卸载说明](#卸载说明)

---

## 前置条件

- 已安装并配置好WSL2
- Ubuntu 20.04 LTS 或更新版本的Linux发行版
- 稳定的网络连接
- 足够的磁盘空间（建议至少10GB可用空间）

---

## 第一步：系统准备

### 1.1 检查必要工具

首先检查系统是否已安装必要的编译工具：

```bash
which wget curl gcc make
```

如果缺少任何工具，使用以下命令安装（需要sudo权限）：

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y wget curl build-essential
```

**注意**：如果系统已有这些工具，可以跳过sudo安装步骤。

---

## 第二步：安装Miniconda

### 2.0 检查Miniconda是否已安装

**首先检查系统中是否已经安装了Miniconda**：

```bash
~/miniconda3/bin/conda --version
```

**如果已安装**，会显示类似输出：
```
conda 25.7.0
```

此时可以**跳过第二步，直接进入[第三步：配置Conda镜像源](#第三步配置conda镜像源)**。

**如果显示"No such file or directory"**，则需要继续以下安装步骤。

---

### 2.1 下载Miniconda安装脚本

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

**下载时间**：约2-5分钟，取决于网络速度（文件大小约155MB）

### 2.2 运行安装脚本

使用静默模式安装（自动接受许可并使用默认路径）：

```bash
bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3
```

**参数说明**：

- `-b`: 静默模式，自动接受许可协议
- `-p ~/miniconda3`: 指定安装路径为家目录下的miniconda3文件夹

**安装时间**：约1-2分钟

### 2.3 初始化Conda

```bash
~/miniconda3/bin/conda init bash
```

**重要**：这会修改`~/.bashrc`文件，添加conda初始化代码。

### 2.4 重新加载Shell环境

```bash
source ~/.bashrc
```

或者关闭并重新打开终端。

### 2.5 验证安装

```bash
~/miniconda3/bin/conda --version
```

**预期输出**：

```
conda 25.7.0
```

或更新版本。

---

## 第三步：配置Conda镜像源

为了加速软件包下载，配置清华大学镜像源。

### 3.1 添加清华镜像源

```bash
~/miniconda3/bin/conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
~/miniconda3/bin/conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
~/miniconda3/bin/conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```

### 3.2 显示频道URL

```bash
~/miniconda3/bin/conda config --set show_channel_urls yes
```

### 3.3 验证配置

```bash
~/miniconda3/bin/conda config --show channels
```

**预期输出**：

```
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```

---

## 第四步：创建专用环境

### 4.1 接受Conda服务条款

首次使用需要接受服务条款：

```bash
~/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
~/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

### 4.2 创建physics环境

```bash
~/miniconda3/bin/conda create -n physics python=3.9 -y
```

**参数说明**：

- `-n physics`: 环境名称为"physics"
- `python=3.9`: 使用Python 3.9版本
- `-y`: 自动确认所有提示

**安装时间**：约2-3分钟

**预期输出**：

```
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##
  environment location: /home/用户名/miniconda3/envs/physics
  ...
done
```

---

## 第五步：安装Geant4和ROOT

### 5.1 安装软件包

激活physics环境并安装Geant4和ROOT：

```bash
source ~/miniconda3/bin/activate physics
conda install geant4=10.7.2 root -c conda-forge -y
```

**参数说明**：

- `geant4=10.7.2`: 指定Geant4版本为10.7.2
- `root`: 安装ROOT最新兼容版本（6.26.04）
- `-c conda-forge`: 从conda-forge频道获取软件包

**安装时间**：约10-30分钟，取决于网络速度

**下载大小**：约1.88GB

**重要软件包**：

- Geant4 10.7.2 及所有数据文件（约1GB）
- ROOT 6.26.04
- Qt 5.12.9（可视化支持）
- OpenGL支持库
- 编译器工具链（gcc 10.4.0, g++, gfortran）

### 5.2 安装CMake和Make

为了编译例子程序，还需要安装cmake：

```bash
conda install cmake make -c conda-forge -y
```

**安装时间**：约1-2分钟

---

## 第六步：验证安装

### 6.1 验证Geant4

```bash
source ~/miniconda3/bin/activate physics
geant4-config --version
```

**预期输出**：

```
10.7.2
```

### 6.2 验证ROOT

```bash
root-config --version
```

**预期输出**：

```
6.26/04
```

### 6.3 测试ROOT Python绑定

```bash
python -c "import ROOT; print('ROOT Python binding works!')"
```

**预期输出**：

```
ROOT Python binding works!
```

### 6.4 查看Geant4库链接信息

```bash
geant4-config --libs | head -c 200
```

**预期输出示例**：

```
-L/home/用户名/miniconda3/envs/physics/bin/../lib -lG4OpenGL -lG4gl2ps -lG4Tree -lG4FR -lG4GMocren -lG4visHepRep -lG4RayTracer -lG4VRML -lG4vis_management -lG4modeling...
```

---

## 第七步：测试B1例子

### 7.1 创建工作目录

```bash
mkdir -p /mnt/c/Songtan/MyGeant4/MyG4
```

### 7.2 复制B1例子

```bash
cp -r ~/miniconda3/envs/physics/share/Geant4-10.7.2/examples/basic/B1 /mnt/c/Songtan/MyGeant4/MyG4/
```

### 7.3 创建构建目录

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1
mkdir build
cd build
```

### 7.4 配置CMake

```bash
source ~/miniconda3/bin/activate physics
cmake ..
```

**预期输出**（最后几行）：

```
-- Found OpenGL: /path/to/libGL.so
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Songtan/MyGeant4/MyG4/B1/build
```

### 7.5 编译

```bash
make -j4
```

**参数说明**：

- `-j4`: 使用4个并行作业加速编译

**编译时间**：约30秒-1分钟

**预期输出**：

```
[ 12%] Building CXX object CMakeFiles/exampleB1.dir/exampleB1.cc.o
[ 25%] Building CXX object CMakeFiles/exampleB1.dir/src/B1ActionInitialization.cc.o
...
[100%] Linking CXX executable exampleB1
[100%] Built target exampleB1
```

### 7.6 运行B1例子并测试可视化

#### 7.6.1 交互式可视化模式（推荐）

**重要提示：CMake 已自动复制宏文件到 build 目录**

B1 例子的 CMakeLists.txt 已配置为自动将所有宏文件（`.mac`）复制到 build 目录，因此**推荐从 build 目录直接运行程序**。

**最佳运行方式（从 build 目录）**：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1/build  # 进入 build 目录
source ~/miniconda3/bin/activate physics
./exampleB1  # 直接运行，宏文件已在当前目录
```

**或者从B1根目录运行**：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1  # 进入 B1 根目录
source ~/miniconda3/bin/activate physics
./build/exampleB1  # 从 B1 根目录运行 build 中的可执行文件
```

**为什么推荐从 build 目录运行？**

查看 `CMakeLists.txt` 第42-61行可以看到：
```cmake
# Copy all scripts to the build directory, i.e. the directory in which we
# build B1. This is so that we can run the executable directly because it
# relies on these scripts being in the current working directory.
```

CMake 设计意图就是让你从 build 目录运行程序：
- ✅ 宏文件已复制到 build 目录
- ✅ 修改 build 目录的宏文件可立即测试
- ✅ 修改源目录的宏文件后，`make` 会自动同步
- ✅ 输出文件（.root/.csv）也在 build 目录，方便管理

**程序启动后会自动**：

- 初始化Geant4
- 打开OpenGL可视化窗口（600x600像素）
- 显示探测器几何结构（Envelope、Shape1、Shape2）
- 显示坐标轴（x=红色、y=绿色、z=蓝色）
- 显示比例尺、Geant4 logo等装饰元素

**窗口操作**：

-  鼠标左键拖动：旋转视角
-  鼠标滚轮：缩放视图

**运行粒子模拟**：
在交互式命令行 `Idle>` 提示符下输入：

```
Idle> /run/beamOn 10
```

可视化窗口会实时显示10个粒子事件的轨迹动画。

**退出程序**：

```
Idle> exit
```

**注意**：WSL2环境下关闭窗口时可能出现 `Segmentation fault`，这是正常的X11转发问题，不影响程序功能和数据，可以安全忽略。

#### 7.6.2 批处理模式（无可视化）

使用宏文件运行模拟，不打开可视化窗口：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1/build
./exampleB1 run1.mac
```

**预期输出**（最后几行）：

```
G4WT1 > --------------------End of Local Run------------------------
G4WT0 > --------------------End of Local Run------------------------
--------------------End of Global Run-----------------------
...
RunManagerKernel is deleted. Good bye :)
```

**说明**：如果看到"Good bye :)"，表示程序运行成功。

#### 7.6.3 编译与重新编译说明

**何时需要 make clean？**

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1/build

# ✅ 必须 clean 的情况：
# 1. 修改了 CMakeLists.txt
make clean && cmake .. && make

# 2. 添加/删除了源文件或头文件
make clean && cmake .. && make

# 3. 修改了头文件中的类定义
make clean && make

# 4. 编译出现奇怪错误
make clean && make
```

```bash
# ✅ 只需 make 的情况：
# 1. 只修改了 .cc 源文件
make

# 2. 修改了宏文件 (.mac)
make  # 自动复制到 build 目录
# 或直接运行（宏文件运行时加载）
./exampleB1
```

**快速决策**：
- 修改代码 → `make`
- 改了头文件/CMakeLists.txt → `make clean && make`
- 出错了 → `make clean && make`

#### 7.6.4 检查可视化驱动（可选）

验证系统支持的可视化驱动：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1/build
./exampleB1 2>&1 | head -30
```

**预期输出**：

```
Available UI session types: [ Qt, GAG, tcsh, csh ]

**************************************************************
 Geant4 version Name: geant4-10-07-patch-02 [MT]
  << in Multi-threaded mode >>
...
Registered graphics systems are:
  ASCIITree (ATree)
  DAWNFILE (DAWNFILE)
  G4HepRep (HepRepXML)
  G4HepRepFile (HepRepFile)
  RayTracer (RayTracer)
  VRML1FILE (VRML1FILE)
  VRML2FILE (VRML2FILE)
  gMocrenFile (gMocrenFile)
  OpenGLImmediateQt (OGLIQt, OGLI)
  OpenGLStoredQt (OGLSQt, OGL, OGLS)
  OpenGLImmediateX (OGLIX, OGLIQt_FALLBACK)
  OpenGLStoredX (OGLSX, OGLSQt_FALLBACK)
```

**重要信息**：

- ✅ Qt可视化驱动已注册
- ✅ OpenGL驱动可用
- ✅ 多线程模式启用

#### 7.6.5 自定义可视化宏文件（可选）

创建自定义可视化脚本：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1
cat > custom_vis.mac << 'EOF'
# 自定义可视化设置
/run/initialize

# 打开OpenGL可视化窗口
/vis/open OGL 800x600-0+0

# 绘制探测器几何
/vis/drawVolume

# 设置视角
/vis/viewer/set/autoRefresh true
/vis/viewer/set/viewpointVector 1 1 1
/vis/viewer/set/upVector 0 0 1

# 添加坐标轴（原点，长度1米）
/vis/scene/add/axes 0 0 0 1 m

# 添加粒子轨迹
/vis/scene/add/trajectories smooth
/vis/modeling/trajectories/create/drawByCharge
/vis/modeling/trajectories/drawByCharge-0/default/setDrawStepPts true
/vis/modeling/trajectories/drawByCharge-0/default/setStepPtsSize 2

# 累积显示事件
/vis/scene/endOfEventAction accumulate

# 设置为表面显示模式
/vis/viewer/set/style surface

# 运行20个事件
/run/beamOn 20
EOF
```

运行自定义可视化：

```bash
cd /mnt/c/Songtan/MyGeant4/MyG4/B1/build
# make 会自动将 custom_vis.mac 复制到 build 目录
make
./exampleB1 custom_vis.mac
```

**注意**：在WSL2环境中，Qt可视化可能会回退到OpenGL X11模式，这是正常的，不影响可视化功能。

---

## 常见问题

### Q1: 下载速度很慢怎么办？

**A**: 可以尝试中科大镜像源：

```bash
~/miniconda3/bin/conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
~/miniconda3/bin/conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
~/miniconda3/bin/conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
```

### Q2: 安装失败怎么办？

**A**: 清理缓存并重试：

```bash
source ~/miniconda3/bin/activate physics
conda clean --all
conda update conda
# 然后重新运行安装命令
```

### Q3: 版本冲突怎么办？

**A**: 指定具体版本：

```bash
conda install geant4=10.7.2 root=6.26 -c conda-forge -y
```

### Q4: 如何每次自动激活physics环境？

**A**: 在`~/.bashrc`中添加：

```bash
echo "conda activate physics" >> ~/.bashrc
source ~/.bashrc
```

### Q5: 可视化窗口无法显示？

**A**: 这在WSL2中是正常的，有以下解决方案：

1. **使用WSLg**（Windows 11）：自动支持GUI应用
2. **使用X11转发**：安装VcXsrv或Xming
3. **使用批处理模式**：不需要GUI，适合大规模计算
4. **使用VRML等文件输出**：生成文件后在Windows中查看

### Q6: Qt可视化为什么会fallback到OpenGL X11？

**A**: 这是WSL2环境的限制，但不影响使用：

- OpenGL X11驱动功能完整
- 可以正常显示几何体和粒子轨迹
- Qt库已安装，只是GUI后端的差异

### Q7: 需要的磁盘空间是多少？

**A**:

- Miniconda: ~500MB
- Physics环境（含Geant4+ROOT）: ~5GB
- 建议总空间: 10GB+

### Q8: 支持多线程吗？

**A**: 是的，Geant4编译为多线程模式（MT），可以在宏文件中设置：

```
/run/numberOfThreads 4
```

### Q9: 关闭可视化窗口时出现"Segmentation fault"错误？

**A**: 这是WSL2环境中的正常现象，不影响使用：

**原因**：

- WSL2的图形转发（X11/Wayland）与Qt/OpenGL清理过程存在兼容性问题
- 只在关闭窗口或程序退出时出现
- 程序运行、计算和可视化显示都是正常的

**解决方案**：

1. **忽略这个错误**（推荐）- 不影响任何功能
2. **使用命令退出** - 在交互式命令行输入 `exit` 而不是直接关闭窗口
3. **使用批处理模式** - 运行宏文件后自动退出，没有这个问题

**验证程序正常**：

- 可视化窗口能正常显示 ✓
- 粒子轨迹能正确显示 ✓
- 模拟数据正确计算 ✓
- 输出文件完整保存 ✓

---

## 卸载说明

### 完全卸载所有内容

```bash
# 1. 删除conda环境
~/miniconda3/bin/conda env remove -n physics

# 2. 删除Miniconda
rm -rf ~/miniconda3

# 3. 删除工作目录（可选）
rm -rf /mnt/c/Songtan/MyGeant4/MyG4

# 4. 清理.bashrc中的conda配置
# 手动编辑 ~/.bashrc，删除以下内容：
# >>> conda initialize >>>
# ... conda相关代码 ...
# <<< conda initialize <<<

# 5. 删除.condarc配置文件
rm -f ~/.condarc

# 6. 重新加载shell
source ~/.bashrc
```

### 只删除physics环境

```bash
~/miniconda3/bin/conda env remove -n physics
```

---

## 环境变量说明

安装完成后，physics环境包含的重要环境变量：

```bash
source ~/miniconda3/bin/activate physics

# 查看Geant4相关路径
echo $G4INSTALL
echo $G4DATA

# 查看库路径
echo $LD_LIBRARY_PATH

# 查看可执行文件路径
echo $PATH
```

---

## 系统要求总结

| 项目   | 要求                   |
| ---- | -------------------- |
| 操作系统 | WSL2 + Ubuntu 20.04+ |
| 磁盘空间 | 至少10GB可用             |
| 内存   | 建议4GB+               |
| 网络   | 稳定连接，需下载约2GB数据       |
| 时间   | 总计约20-40分钟           |

---

## 已安装软件版本清单

完成安装后，您将拥有以下软件：

| 软件        | 版本      |
| --------- | ------- |
| Miniconda | 25.7.0+ |
| Python    | 3.9.15  |
| Geant4    | 10.7.2  |
| ROOT      | 6.26.04 |
| Qt        | 5.12.9  |
| CMake     | 3.25.1  |
| GCC       | 10.4.0  |
| OpenGL    | 已支持     |

---

## 下一步

安装完成后,您可以：

1. **测试可视化功能**：

   ```bash
   cd /mnt/c/Songtan/MyGeant4/MyG4/B1
   source ~/miniconda3/bin/activate physics
   ./build/exampleB1  # 启动交互式可视化
   ```

   - 在可视化窗口中旋转、缩放探测器
   - 运行命令 `/run/beamOn 10` 查看粒子轨迹
   - 尝试不同的可视化命令和设置

2. **学习Geant4基础**：

   - 研究B1例子的源代码（`/mnt/c/Songtan/MyGeant4/MyG4/B1/src/` 和 `/mnt/c/Songtan/MyGeant4/MyG4/B1/include/`）
   - 阅读Geant4官方文档
   - 理解探测器构建、物理列表、动作初始化等概念
   - 尝试修改B1例子的几何、材料或物理过程

3. **探索其他例子**：
   
   ```bash
   ls ~/miniconda3/envs/physics/share/Geant4-10.7.2/examples/
   ```
   
   - B2-B5：其他基础例子，逐步增加复杂度
   - extended：扩展例子，展示高级功能
   - advanced：高级应用示例

4. **开发自己的应用**：
   
   - 使用B1作为模板创建新项目
   - 设计自己的探测器几何
   - 定义特定的物理过程
   - 实现自定义的数据记录和分析

5. **使用ROOT分析数据**：
   
   - 启动ROOT交互环境：`root`
   - 使用Python接口：`import ROOT`
   - 学习数据可视化和统计分析
   - 创建直方图、拟合曲线等

6. **优化和调试**：
   
   - 学习使用多线程模式提高性能
   - 调整可视化设置和渲染选项
   - 使用批处理模式进行大规模模拟
   - 输出数据到文件进行离线分析

---

## 参考资源

- **Geant4官方文档**: https://geant4.web.cern.ch/
- **ROOT官方文档**: https://root.cern/
- **Conda文档**: https://docs.conda.io/
- **清华镜像帮助**: https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

---

## 更新日志

- **2025-10-10 v1.1**:
  
  - 增强第七步：添加详细的可视化启动说明
  - 新增交互式模式操作指南（7.6.1）
  - 新增自定义可视化宏文件示例（7.6.4）
  - 添加Q9：解释WSL2环境中的Segmentation fault问题
  - 优化"下一步"部分，添加可视化测试和更多学习建议

- **2025-10-10 v1.0**:
  
  - 初始版本，基于实际安装测试
  - 完整的Miniconda + Geant4 + ROOT安装流程
  - B1例子编译和运行验证

- **环境**: WSL2 Ubuntu, Linux 5.15.167.4-microsoft-standard-WSL2

---

**祝您使用愉快！如有问题，请参考常见问题部分或查阅官方文档。**
