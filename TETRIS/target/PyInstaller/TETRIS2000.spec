# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/home/papalooo/Game/TETRIS2000/src/main/python/main.py'],
             pathex=['/home/papalooo/Game/TETRIS2000/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/papalooo/Game/TETRIS2000/venv/lib/python3.9/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/papalooo/Game/TETRIS2000/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='TETRIS2000',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='TETRIS2000')
