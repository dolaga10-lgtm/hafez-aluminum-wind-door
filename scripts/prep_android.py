import os, shutil
from PIL import Image
res = 'android/app/src/main/res'
src = Image.open('www/icon-512.png').convert('RGBA')
for d, n in {'mipmap-mdpi':48,'mipmap-hdpi':72,'mipmap-xhdpi':96,'mipmap-xxhdpi':144,'mipmap-xxxhdpi':192}.items():
    p = os.path.join(res, d); os.makedirs(p, exist_ok=True)
    for name in ('ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png'):
        src.resize((n,n), Image.LANCZOS).save(os.path.join(p, name))
shutil.rmtree(os.path.join(res,'mipmap-anydpi-v26'), ignore_errors=True)
d = 'android/app/src/main/java/com.hafez.aluminum'; os.makedirs(d, exist_ok=True)
open(os.path.join(d,'MainActivity.java'),'w').write('''package com.hafez.aluminum;
import android.os.Bundle;
import android.view.WindowManager;
import com.getcapacitor.BridgeActivity;
public class MainActivity extends BridgeActivity {
  @Override public void onCreate(Bundle b) {
    super.onCreate(b);
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
  }
}
''')
