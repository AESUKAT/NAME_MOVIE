a1,a2,a3,a4=1,1,0,0  # 加速度として使う変数
A=150                # 周期の変数
t_n=0                # 角度の変数
now=0                # 現在の時間の100分率
f=0                  # フレーム数
                     # anの中に三角関数を置き、三角関数の変数としてtを利用する
                     # t内では定数PI/Aに変数fをかけて利用し
                     # 座標に変位*anを足すことで曲線的に動かせる
root=255             # 吹き飛ばされた世界(以下:真世界)を認識できるかどうかを判別する変数
                     # 0で認識でき、255で認識することはできない
bamen=0              # 場面の順番
                     # ## は関数内の処理順に関するメモ

def setup():        # setupを行う
    size(1280,720)  # 画面サイズを1280,720に設定
    frameRate(100)  # フレームレートを100に設定
    now=millis()    # nowをmillis()に設定

def draw():                                         # 後述の関数を描画する
    global a1,a2,a3,a4,A,bamen,now,f                # globalの設定
    
     # ENTER key を押すと始まる という表記
    if bamen==0:                                    # 場面0なら以下を実行する
     # 1/100秒ごとにfを1増やしフレームカウントとして使う
        if now%10==0:
            f+=1
        t=PI/A*f                                    # 時間が経つごとにtが増える
        a1=cos(t)                                   # tの増加に合わせて-1<=a1<=1を往復する
         # 真世界を認識できる者のスタート画面
        if root==0:
            background(255-root)                    # 真世界を認識できるなら白背景に
            noStroke()                              # 縁を消す
            fill(0+root,128+127*a1)                 # textを点滅させる
            textSize(50)                            # テキストサイズを50に設定
            text('Please press ENTER key',350,600)  # ENRERを押す労力を要求する
         # 真世界を認識できない者への忠告
        if root==255:
            background(255-root)                    # 真世界を認識できないなら黒背景に
            noStroke()                              # 縁を消す
            fill(0+root,128+127*a1)                 # textを点滅させる
            textSize(50)                            # テキストサイズを50に設定
            text('Please press ENTER key',350,600)  # ENRERを押す労力を要求する
            stroke(0+root,128+127*a1)               # lineを点滅させる
            line(300,580,950,580)                   # ENTERを押してはならない忠告
            fill(255,0,0,190+65*sin(PI/(A+200)*f))  # textを赤点滅
             # SPACEを押さなければ吹き飛ばされた世界を認識することはできない
            text("Press SPACE key, or you won't win!!",220,height/2)

     # 4つの四角形が背景を作る
    if bamen==1:             # 場面1なら以下を実行する
         # 1/100秒ごとにfを1増やしフレームカウントとして使う
        if now%10==0:
            f+=1
        background(255-root) # 真世界を認識できるなら白、できないなら黒背景に
        A=350                # sin,cosの周期を700フレームに決定
        t1=PI/A*f            # fの増加によってt1も増加する
        a1=sin(t1)           # t1の増加によりsinも-1<=a1<=1の間を単振動する
        t2=t1-PI/4           # t2はt1より1/8周期遅れる
        a2=sin(t2)           # a1に同じ
        t3=t2-PI/4           # t3はt2より1/8周期遅れる
        a3=sin(t3)           # a1に同じ
        t4=t3-PI/4           # t4はt3より1/8周期遅れる
        if t1>=PI/2:         # t1の範囲をPI/2以下に固定し
            t1=PI/2          # それ以上増えないように固定する
            a1=sin(t1)       # a1の更新
        if t2>=PI/2:         # t2の範囲をPI/2以下に固定し
            t2=PI/2          # それ以上増えないように固定する
            a2=sin(t2)       # a2の更新
            a4=sin(t4)       # 赤い四角が出てから黄色い四角が描画される
        if t3>=PI/2:         # t3の範囲をPI/2以下に固定し
            t3=PI/2          # それ以上増えないように固定する
            a3=sin(t3)       # a3の更新
        if t4>=PI/2:         # t4の範囲をPI/2以下に固定し
            t4=PI/2          # それ以上増えないように固定する
            a4=sin(t4)       # a4の更新
            bamen=2          # 次の場面へ進む
            f=0              # fのリセット
         # 4つの4色の四角形が順番に出てくる
        kaimaku(width/2,height/2)
    
     # 場面を切り替える
    if bamen==2:                    # 場面2なら以下を実行する
         # 1/100秒ごとにfを1増やしフレームカウントとして使う
        if now%10==0:
            f+=1
        background(255-root)        # 真世界を認識できるなら白、できないなら黒背景に
        back(width/2,height/2)      # 背景に4色の四角形を表示
        A=250                       # sin,cosの周期を250に設定
        t5=PI/A*f                   # fの増加によってt5も増加する
        a1=1                        # a1を1に固定
        a3=cos(t5)                  # t5の増加によりcosも-1<=a3<=1の間を単振動する
        a4=sin(t5)                  # t5の増加によりsinも-1<=a4<=1の間を単振動する
         # nameBOXを表示するための黒枠が出現する
        kirikae(width/2+200*a4*a4,height/2+200*a4*a4)
        kakurenbo(width/2,height/2) # 隠れている下の名前と肉球の表示、kirikaeによって見える
        if f>=250:                  # 250フレームで場面2を終える
            bamen=3                 # 次の場面へ進む
    
     # 名前に変形する箱が現れる
    if bamen==3:                    # 場面3なら以下を実行する
         # 1/100秒ごとにfを1増やしフレームカウントとして使う
        if now%10==0:
            f+=1
        background(255)             # 背景を白に設定
        A=250                       # sin,cosの周期を250に設定
        t5=PI/A*f                   # fの増加によってt5も増加する
        a1=1                        # a1を1に固定
        a3=cos(t5)                  # t5の増加によりcosも-1<=a3<=1の間を単振動する
        a4=sin(t5)                  # t5の増加によりsinも-1<=a4<=1の間を単振動する
        back(width/2,height/2)      # 背景に4色の四角形を表示
        nameBOX(width/2,height/2)   # 名前に変形する箱の表示
        if 495<f<498:               # 495-498フレームの間に以下を描画
            king1(0,0)              # 不吉な予兆が現れては消える
         # nameBOXを表示するための黒枠が出現する
        kirikae(width/2-200*a4*a4,height/2+200*a4*a4*a4)
        kakurenbo(width/2,height/2) # 隠れている下の名前と肉球の表示、kirikaeによって見える
        if f>=500:                  # 500フレームで場面3を終える
            bamen=4                 # 次の場面へ進む
            f=0                     # fのリセット

     # 背景を消し飛ばし四角がKAMATAになる
     # root=0のときのみ真世界を認識できる
    if bamen==4:                               # 場面4なら以下を実行する
        f2=0                                   # 吹き飛ぶ背景用のフレームカウント
        f3=0                                   # 浮き出る文字用のフレームカウント
        f4=0                                   # 動きの軌跡用のフレームカウント
         # 1/100秒ごとにfを1増やしフレームカウントとして使う
        if now%10==0:
            f+=1
        for i in range(120):                   # iを120回繰り返す
            strokeWeight(3)                    # 線の太さを3に設定
            stroke(2*i,0,2*i)                  # i番目の線の色を(2*i,0,2*i)に設定
            line(0,3*i,width,3*i)              # i番目の線を(0,3*i,width,3*i)に描画
        for i in range(120):                   # iを120回繰り返す
            stroke(238-i,0,238-i)              # i番目の線の色を(238-i,0,238-i)に設定
            line(0,360+3*i,width,360+3*i)      # i番目の線を(0,360+3*i,width,360+3*i)に描画
        A=400                                  # sin,cosの周期を400に設定
        a2=0                                   # a2を0に固定
        hosi(30*cos(PI/300*f),30*cos(PI/300*f))         # 真世界の星を描画
        if 0<=f<=19:                           # 0-19フレームの間に以下を表示する
            back(width/2,height/2)             # 背景に4色の四角形を表示
        elif 19<f<=25:                         # 19-25フレームの間に以下を表示する
            hukitobu(width/2,height/2)         # 背景に4色の割れた四角形を表示
        elif 26<f<=75:                         # 25-75フレームの間に以下を表示する
            a=sin(PI/7*f)                      # fの増加によりsinも-1<=a1<=1の間を単振動する
            hukitobu(width/2+4*a*a*a,height/2+4*a*a)    # 背景の割れた4色の四角形が揺れる
        elif 75<f:                             # 75-フレーム以降のbamen4中に以下を表示する
            a=sin(PI/10*f)                     # fの増加によりsinも-1<=a<=1の間を単振動する
            f2=f-75                            # f2をfから75フレーム遅れに設定する
            a2=sin(PI/700*f2)                  # f2の増加によりsinも増加する
            if PI/700*f2>PI/2:                 # a2の変数の範囲をPI/2以下に固定し
                a2=1                   # a2の変数の範囲がPI/2より大きいとき、a2を0に固定する
            hukitobu(width/2+4*a*a*a,height/2+4*a*a)    # 背景にあった4色の四角形が吹き飛ぶ
        if 11<f<13 or 16<f<19 or 24<f<27:      # 11-13,16-19,24-27フレームの間に以下を表示する
            king3(0,0)                         # 不吉な予兆が奥に現れては消える
        if 21<f<24 or 63<f<70 or 555<f<565:  # 21-24,63-70,555-565フレームの間に以下を表示する
            king4(0,0)                         # 不吉な予兆が奥に現れては消える
        if 14<f<16 or 516<f<519:               # 14-16,516-519フレームの間に以下を表示する
            king2(0,0)                         # 不吉な予兆が奥に現れては消える
        if 545<f<547:                          # 545-547フレームの間に以下を表示する
            king3(0,0)                         # 不吉な予兆が奥に現れては消える
        if 0<=f<=25:                           # 0-25フレームの間に以下を表示する
            nameBOX(width/2,height/2)          # 名前に変形する箱の表示
        if 25<f<=170:                          # 25-170フレームの間に以下を表示する
            a=sin(PI/(4+f/5)*f)                # fの増加によりsinも-1<=a<=1の間を単振動する
            nameBOX(width/2+3*a*a*a,height/2+3*a*a)     # 名前に変形する箱が振動する
        if 25<f<90:                            # 25-90フレームの間に以下を表示する
            noStroke()                         # 縁を消す
            fill(255,random(40,100))         # 色を白に固定し透明度を40-100でランダムに変化
            rect(0,0,width,height)             # 画面いっぱいに四角形を描画
        elif 170<f:                            # 170-フレーム以降の場面4に以下を表示する
            f3=f-170                           # f3をfから170フレーム遅れに設定する
            a1=cos(PI/700*f3)                  # f3の増加によりcosは減少する
            if PI/700*f3>PI/2:                 # a1の変数の範囲をPI/2以下に固定し
                a1=0                   # a1の変数の範囲がPI/2より大きいとき、a1を0に固定する
            nameBOX(width/2+20*sin(PI/300*f3),height/2) # 箱が名前に変形する
            nameB(width/2+20*sin(PI/300*f3),height/2)   # 箱の内側や外側に影ができる
        if 160<f:                              # 160-フレーム以降の場面4に以下を表示する
            f4=f-160                           # f4をfから160フレーム遅れに設定する
            a4=cos(PI/700*f4)                  # f4の増加によりcosは減少する
            nameC(width/2+20*sin(PI/300*f4),height/2)   # 箱が変形する動きの軌跡を表示する
        if 530<f<532 or 535<f<538:             # 530-532,535-538フレームの間に以下を表示する
            king1(0,0)                         # 不吉な予兆が手前に現れては消える
        if 0<f<3 or 520<f<524:                 # 0-3,520-524フレームの間に以下を表示する
            king2(0,0)                         # 不吉な予兆が手前に現れては消える
        if 8<f<14 or 542<f<544 or 548<f<553: # 8-14,542-544,548-553フレームの間に以下を表示する
            king3(0,0)                         # 不吉な予兆が手前に現れては消える
        if 29<f<33:                            # 29-33フレームの間に以下を表示する
            king4(0,0)                         # 不吉な予兆が手前に現れては消える
        if 565<f:                              # 565フレームで場面2を終える
            bamen=5                            # 次の場面へ進む
            f=0                                # fのリセット
         # 真世界を認識できない者は何もできずに結果だけを認識する
        if f>=19 and root==255:                # 19フレームで場面4を吹き飛ばされる
            bamen=5                            # 次の場面へ進む
            f=0                                # fのリセット
    
     # 場面5以上でbamenを2で割ったあまりが1なら以下を実行する
    if bamen>=5 and bamen%2==1:
        for i in range(120):              # iを120回繰り返す
            strokeWeight(2)               # 線の太さを2に設定
            stroke(110+i,110,110+i)       # i番目の線の色を(110+i,110,110+i)に設定
            line(0,3*i,width,3*i)         # i番目の線を(0,3*i,width,3*i)に描画
        for i in range(120):              # iを120回繰り返す
            stroke(219-i,110,219-i)       # i番目の線の色を(219-i,110,219-i)に設定
            line(0,360+3*i,width,360+3*i) # i番目の線を(0,360+3*i,width,360+3*i)に描画
        nameA(width/2,height/2)           # 内側の透けた名前の表示
        back2(width/2,height/2)           # 名前に被らないように4色の四角形を背景の上に描画
        namaeA(width/2-30,height/2-50)    # カタカナでカマタを表示
    
     # 場面5以上でbamenを5で割ったあまりが0なら以下を実行する
    if bamen>=5 and bamen%2==0:
        a=sin(TWO_PI/10*frameCount)   # frameCountの増加によってsinも-1<=a<=1を単振動する
        for i in range(240): #iを240回繰り返す
             # i番目の線の色を(random(0,255),random(0,255),random(0,255))に設定
            stroke(random(0,255),random(0,255),random(0,255))
            strokeWeight(2)           # 線の太さを2に設定
            line(0,3*i,width,3*i)     # i番目の線を(0,3*i,width,3*i)に描画
        nameD(width/2+30*a,height/2)  # KAMATAが左右にダンシング
        namaeB(width/2,height/2)      # カマタが元気よく荒ぶる

def keyPressed():           # ENTERまたはSPACEを押すと変化する
    global bamen,f,root     # globalの設定
     # 真世界を認識できる力を与える
    if root==255 and bamen==0 and key==' ' :
        root-=255
     # すべてが始まる
    if bamen==0 and key==ENTER:
        bamen=1
        f=0
     # 真世界を認識できる者のみが使える隠しコード
    if root==0 and bamen>=5 and key==' ':
        bamen+=1
        f=0

def kaimaku(x,y): # ENTERキーを押すと飛び出してきて画面をカラフルにする
    noStroke()
    fill(128,50)
    rect(x-600,y-360,300,760*a3) ##3 #赤い四角の影
    fill(255,128,128)
    rect(x-640,y-400,300,760*a3) ##3 #赤の四角
    fill(128,255,128)
    rect(x-640,y+60,1280*a2,300) ##2 #緑の四角
    fill(0,128,255)
    rect(x+340,y-360,300,720*a1) ##1 青い四角
    fill(128,50)
    rect(x-340,y-320,1020*a4,300) ##4 #黄色い四角の影
    fill(255,255,130)
    rect(x-340,y-360,1020*a4,300) ##4 #黄色い四角

def back(x,y): # kaimakuの変化なし版
    noStroke()
    fill(128,50)
    rect(x-600,y-360,300,760) ##3 #赤い四角の影
    fill(255,128,128)
    rect(x-640,y-400,300,760) ##3 #赤の四角
    fill(128,255,128)
    rect(x-640,y+60,1280,300) ##2 #緑の四角
    fill(0,128,255)
    rect(x+340,y-360,300,720) ##1 青い四角
    fill(128,50)
    rect(x-340,y-320,1020,300) ##4 #黄色い四角の影
    fill(255,255,130)
    rect(x-340,y-360,1020,300) ##4 #黄色い四角

def back2(x,y): # 最後に出てくる4色の背景
     # 赤の頂点を設定
    noStroke()
    fill(255,128,128)
    beginShape()
    x=0;y=0
    vertex(x,y)
    x=x+width/2-380;y=y+height/2-150
    vertex(x+40,y-210)
    vertex(x+40,y+22)
    vertex(x+22,y-1)
    vertex(x-31,y-1)
    vertex(x-81,y+210)
    vertex(x-260,y+210)
    endShape()
     # 緑の頂点を設定
    fill(128,255,128)
    beginShape()
    vertex(x-260,y+210)
    vertex(x-81,y+210)
    y=y+300
    vertex(x-102,y)
    vertex(x+30,y+150)
    vertex(x+720,y+150)
    vertex(x+720,y+210)
    vertex(x-260,y+210)
    endShape()
     # 青の頂点を設定
    fill(0,128,255)
    beginShape()
    vertex(x+720,y+150)
    vertex(x+720,y+210)
    x=x+772
    vertex(x+248,y+210)
    vertex(x+248,y-210)
    vertex(x+79,y-210)
    vertex(x+118,y)
    vertex(x-15,y+150)
    endShape()
     # 黄色の頂点を設定
    fill(255,255,130)
    beginShape()
    vertex(x+248,y-210)
    vertex(x+79,y-210)
    y=y-300
    vertex(x+60,y-1)
    x=x-280
    x=x-57
    vertex(x+53.5,y-1)
    vertex(x-2.5,y-103)
    x=x-155
    vertex(x+152.5,y-103)
    vertex(x+78.5,y+88)
    vertex(x,y-1)
    x=x-155
    x=x-125
    vertex(x+118,y)
    vertex(x+59,y+50)
    vertex(x+39,y+22)
    vertex(x+40,y-210)
    x=x+772
    vertex(x+248,y-210)
    endShape()

def kakurenbo(x,y): # 画面が暗転すると名前と肉球が隠れている
     # 下の名前と肉球の表示
    noStroke()
    x=x-600
    y=y-250
     # タの頂点を設定
    fill(255,128,128)
    beginShape()
    vertex(x+40,y-10)
    vertex(x+180,y-20)
    vertex(x+75,y+250)
    vertex(x+140,y)
    vertex(x+60,y)
    vertex(x+30,y+70)
    vertex(x,y+60)
    vertex(x+40,y-10)
    endShape()
    beginShape()
    vertex(x+35,y+20)
    vertex(x+150,y+40)
    vertex(x+140,y+70)
    vertex(x+40,y+30)
    endShape()
     # クの頂点を設定
    y=y+350
    fill(128,255,128)
    beginShape()
    vertex(x+40,y-10)
    vertex(x+180,y-20)
    vertex(x+75,y+250)
    vertex(x+140,y)
    vertex(x+60,y)
    vertex(x+30,y+70)
    vertex(x,y+60)
    vertex(x+40,y-10)
    endShape()
     # ミを3つの三角形で表示
    x=x+250
    y=y+70
    triangle(x,y,x+150,y+50,x,y+20)
    y=y+60
    triangle(x,y,x+150,y+50,x,y+20)
    y=y+60
    triangle(x,y,x+150,y+50,x,y+20)
     # 肉球を3つの小さい円と1つの大きい円で3つ表示
    fill(0,128,255)
    x=x+400
    y=y-300
    ellipse(x+410,y+200,40,40)
    ellipse(x+480,y+170,40,40)
    ellipse(x+550,y+190,40,40)
    ellipse(x+490,y+270,100,100)
    fill(255,255,130)
    ellipse(x-20,y-300,40,40)
    ellipse(x+50,y-330,40,40)
    ellipse(x+120,y-310,40,40)
    ellipse(x+60,y-230,100,100)
    ellipse(x+230,y-285,50,50)
    ellipse(x+300,y-315,50,50)
    ellipse(x+370,y-295,50,50)
    ellipse(x+310,y-215,120,120)

def kirikae(x,y):  # 画面切り替え用の黒い枠が出てくる
     # 黒い四角が周りから中心に向かってやってくるイメージ
     # 画面四隅と空洞となる四角形の頂点を設定
     # 影
    noStroke()
    fill(0,50)
    beginShape()
    vertex(0,0)
    vertex(0,height)
    vertex(width,height)
    vertex(width,0)
    vertex(x+390+350*a3,y-310-350*a3)
    vertex(x+390+350*a3,y+390+350*a3)
    vertex(x-310-350*a3,y+390+350*a3)
    vertex(x-310-350*a3,y-310-350*a3)
    vertex(x+390+350*a3,y-310-350*a3)
    vertex(width,0)
    endShape()
     # 本体
    fill(0)
    beginShape()
    vertex(0,0)
    vertex(0,height)
    vertex(width,height)
    vertex(width,0)
    vertex(x+350+350*a3,y-350-350*a3)
    vertex(x+350+350*a3,y+350+350*a3)
    vertex(x-350-350*a3,y+350+350*a3)
    vertex(x-350-350*a3,y-350-350*a3)
    vertex(x+350+350*a3,y-350-350*a3)
    vertex(width,0)
    endShape()


def nameA(x,y): # KAMATAの名前が透過されているもの
     # Kの頂点を設定
    x=x-380
    y=y-150
    stroke(0)
    strokeWeight(5)
    noFill()
    beginShape()
    vertex(x-30,y)
    vertex(x-100,y+300)
    vertex(x-30,y+300)
    vertex(x,y+180)
    vertex(x+50,y+300)
    vertex(x+120,y+300)
    vertex(x+30,y+168)
    vertex(x+80,y+120)
    vertex(x+120,y)
    vertex(x,y+96)
    vertex(x+20,y)
    vertex(x-30,y)
    endShape()
     # Aの頂点を設定
    x=x+125
    beginShape()
    vertex(x,y)
    vertex(x-68,y+200)
    vertex(x,y+300)
    vertex(x,y+200)
    vertex(x+45,y+200)
    vertex(x+60,y+300)
    vertex(x+80,y+300)
    vertex(x+150,y)
    vertex(x,y)
    endShape()
    noStroke()
     # Aの▲の影の頂点を設定
    fill(0)
    beginShape()
    vertex(x,y+150)
    vertex(x+50,y+150)
    vertex(x+100,y+50)
    vertex(x+20,y+50)
    vertex(x,y+150)
    endShape()
     # Mの頂点を設定
    x=x+155
    stroke(0)
    noFill()
    beginShape()
    vertex(x,y)
    vertex(x-70,y+300)
    vertex(x-20,y+300)
    vertex(x+30,y+175)
    vertex(x+60,y+300)
    vertex(x+110,y+175)
    vertex(x+130,y+300)
    vertex(x+150,y+300)
    vertex(x+150,y-100)
    vertex(x+75,y+100)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+155
    beginShape()
    vertex(x,y+300)
    vertex(x+50,y+300)
    vertex(x+50,y+200)
    vertex(x+120,y+200)
    vertex(x+160,y+300)
    vertex(x+210,y+300)
    vertex(x,y-100)
    vertex(x,y+300)
    endShape()
    noStroke()
    fill(0)
     # Aの▲の頂点を設定
    beginShape()
    vertex(x+50,y+150)
    vertex(x+100,y+150)
    vertex(x+50,y+50)
    vertex(x+50,y+150)
    endShape()
     # Tの頂点を設定
    x=x+57
    stroke(0)
    noFill()
    beginShape()
    vertex(x,y)
    vertex(x+40,y+70)
    vertex(x+50,y+70)
    vertex(x+165,y+300)
    vertex(x+215,y+300)
    vertex(x+140,y+70)
    vertex(x+260,y+70)
    vertex(x+275,y)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+280
    beginShape()
    vertex(x,y)
    vertex(x-60,y+300)
    vertex(x,y+300)
    vertex(x+20,y+200)
    vertex(x+60,y+200)
    vertex(x+80,y+300)
    vertex(x+115,y+300)
    vertex(x+60,y)
    vertex(x,y)
    endShape()
    noStroke()
     # Aの▲の頂点を設定
    fill(0)
    beginShape()
    vertex(x+25,y+150)
    vertex(x+55,y+150)
    vertex(x+45,y+50)
    vertex(x+20,y+50)
    vertex(x+25,y+150)
    endShape()
     # Kの上側の影の頂点を設定
    x=x-772
    beginShape()
    vertex(x+60,y+50)
    vertex(x,y+96)
    vertex(x+22,y-2)
    endShape()
     # Kの右側の影の頂点を設定
    beginShape()
    vertex(x+30,y+168)
    vertex(x+83,y+119)
    x=x+125
    vertex(x-68,y+203)
    endShape()
     # Mの上側の影の頂点を設定
    x=x+155
    beginShape()
    vertex(x+82,y+87)
    vertex(x+75,y+100)
    vertex(x,y)
    endShape()
     # Kの下側の影の頂点を設定
    x=x-280
    y=y+300
    beginShape()
    vertex(x-104,y)
    vertex(x-30,y)
    vertex(x,y-120)
    vertex(x+50,y)
     # Aの影の頂点を設定
    x=x+125
    vertex(x,y)
    vertex(x,y-100)
    vertex(x+45,y-100)
    vertex(x+60,y)
     # Mの下側の影の頂点を設定
    x=x+155
    vertex(x-20,y)
    vertex(x+30,y-125)
    vertex(x+60,y)
    vertex(x+110,y-125)
    vertex(x+130,y)
      #Aの影の頂点を設定
    x=x+155
    vertex(x+50,y)
    vertex(x+50,y-100)
    vertex(x+120,y-100)
    vertex(x+160,y)
    vertex(x+210,y)
     # Tの影の頂点を設定
    x=x+57
    vertex(x-2,y-300)
    vertex(x,y-300)
    vertex(x+40,y-230)
    vertex(x+50,y-230)
    vertex(x+165,y)
    vertex(x+215,y)
    vertex(x+140,y-230)
    vertex(x+260,y-230)
    vertex(x+275,y-300)
     # Aの影の頂点を設定
    x=x+280
    vertex(x,y-300)
    vertex(x-60,y)
    vertex(x,y)
    vertex(x+20,y-100)
    vertex(x+60,y-100)
    vertex(x+80,y)
    vertex(x+119,y)
    vertex(x-15,y+150)
    x=x-772
    vertex(x+30,y+150)
    endShape()
     # 下側に白ラインを引く
    stroke(255)
    strokeWeight(2)
    line(x-32,y-2,x+105,y+149)
    line(x+118,y-2,x+238,y+149)
    x=x+125
    line(x+79,y-1,x+178,y+149)
    x=x+155
    line(x-20,y-1,x+60,y+149)
    line(x+60,y-3,x+100,y+149)
    x=x+155
    line(x+160,y-1,x+120,y+149)
    x=x+57
    line(x+166,y-1,x+105,y+149)
    x=x+280
    line(x-59,y-1,x-145,y+149)
    line(x+81,y-1,x-50,y+149)

def nameB(x,y): # KAMATAの名前が塗りつぶされているの
     # a1によってただの四角形が名前へと変形する
     # kの頂点を設定
    x=x-380
    y=y-150
    stroke(0)
    strokeWeight(5-5*a1)
    fill(255)
    beginShape()
    vertex(x-30,y)
    vertex(x-100+70*a1,y+300)
    vertex(x-30,y+300)
    vertex(x,y+180+120*a1)
    vertex(x+50,y+300)
    vertex(x+120,y+300)
    vertex(x+30+27*a1,y+168+32*a1)
    vertex(x+80,y+120)
    vertex(x+120,y)
    vertex(x,y+96-96*a1)
    vertex(x+20,y)
    vertex(x-30,y)
    endShape()
     # Aの頂点を設定
    x=x+125
    beginShape()
    vertex(x,y)
    vertex(x-68,y+200)
    vertex(x,y+300)
    vertex(x,y+200+100*a1)
    vertex(x+45,y+200+100*a1)
    vertex(x+60,y+300)
    vertex(x+80,y+300)
    vertex(x+150,y)
    vertex(x,y)
    endShape()
    noStroke()
     # Aの▲の頂点を設定
    fill(0)
    beginShape()
    vertex(x,y+150-100*a1)
    vertex(x+50,y+150-100*a1)
    vertex(x+100,y+50)
    vertex(x+20,y+50)
    vertex(x,y+150-100*a1)
    endShape()
     # Mの頂点を設定
    x=x+155
    stroke(0)
    fill(255)
    beginShape()
    vertex(x,y)
    vertex(x-70,y+300)
    vertex(x-20,y+300)
    vertex(x+30,y+175+125*a1)
    vertex(x+60,y+300)
    vertex(x+110,y+175+125*a1)
    vertex(x+130,y+300)
    vertex(x+150,y+300)
    vertex(x+150,y-100+100*a1)
    vertex(x+75,y+100-100*a1)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+155
    beginShape()
    vertex(x,y+300)
    vertex(x+50,y+300)
    vertex(x+50,y+200+100*a1)
    vertex(x+120,y+200+100*a1)
    vertex(x+160,y+300)
    vertex(x+210,y+300)
    vertex(x,y-100+100*a1)
    vertex(x,y+300)
    endShape()
    noStroke()
     # Aの▲の頂点を設定
    fill(0)
    beginShape()
    vertex(x+50,y+150-100*a1)
    vertex(x+100-50*a1,y+150-100*a1)
    vertex(x+50,y+50)
    vertex(x+50,y+150-100*a1)
    endShape()
     # Tの頂点を設定
    x=x+57
    stroke(0)
    fill(255)
    beginShape()
    vertex(x-57*a1,y)
    vertex(x+40-57*a1,y+70)
    vertex(x+50-67*a1,y+70)
    vertex(x+165-57*a1,y+300)
    vertex(x+215+5*a1,y+300)
    vertex(x+140+140*a1,y+70)
    vertex(x+260+20*a1,y+70)
    vertex(x+275+5*a1,y)
    vertex(x-57*a1,y)
    endShape()
     # Aの頂点を設定
    x=x+280
    beginShape()
    vertex(x,y)
    vertex(x-60,y+300)
    vertex(x,y+300)
    vertex(x+20,y+200+100*a1)
    vertex(x+60,y+200+100*a1)
    vertex(x+80-20*a1,y+300)
    vertex(x+115-55*a1,y+300)
    vertex(x+60,y)
    vertex(x,y)
    endShape()
    noStroke()
     # Aの▲の頂点を設定
    fill(0)
    beginShape()
    vertex(x+25,y+150-100*a1)
    vertex(x+55,y+150-100*a1)
    vertex(x+45,y+50)
    vertex(x+20,y+50)
    vertex(x+25,y+150-100*a1)
    endShape()
     # Kの上側の影の頂点を設定
    x=x-772
    beginShape()
    vertex(x+60-60*a1,y+50-50*a1)
    vertex(x,y+96)
    vertex(x+22-22*a1,y-2+98*a1)
    endShape()
     # Kの右側の影の頂点を設定
    beginShape()
    vertex(x+30+53*a1,y+168-49*a1)
    vertex(x+83,y+119)
    x=x+125
    vertex(x-68+26*a1,y+203-84*a1)
    endShape()
     # Mの上側の影の頂点を設定
    x=x+155
    beginShape()
    vertex(x+82-82*a1,y+87-87*a1)
    vertex(x+75-75*a1,y+100-100*a1)
    vertex(x,y)
    endShape()
     # Kの下側の影の頂点を設定
    x=x-280
    y=y+300
    beginShape()
    vertex(x-104+74*a1,y)
    vertex(x-30,y)
    vertex(x,y-120+120*a1)
    vertex(x+50,y)
     # Aの影の頂点を設定
    x=x+125
    vertex(x,y)
    vertex(x,y-100+100*a1)
    vertex(x+45,y-100+100*a1)
    vertex(x+60,y)
     # Mの下側の影の頂点を設定
    x=x+155
    vertex(x-20,y)
    vertex(x+30,y-125+125*a1)
    vertex(x+60,y)
    vertex(x+110,y-125+125*a1)
    vertex(x+130,y)
     # Aの影の頂点を設定
    x=x+155
    vertex(x+50,y)
    vertex(x+50,y-100+100*a1)
    vertex(x+120,y-100+100*a1)
    vertex(x+160,y)
    vertex(x+210,y)
     # Tの影の頂点を設定
    x=x+57
    vertex(x-2+167*a1,y-300+300*a1)
    vertex(x+165*a1,y-300+300*a1)
    vertex(x+40+125*a1,y-230+230*a1)
    vertex(x+50+115*a1,y-230+230*a1)
    vertex(x+165,y)
    vertex(x+215,y)
    vertex(x+140,y-230+230*a1)
    vertex(x+260-45*a1,y-230+230*a1)
    vertex(x+275-55*a1,y-300+300*a1)
     # Aの影の頂点を設定
    x=x+280
    vertex(x,y-300+300*a1)
    vertex(x-60,y)
    vertex(x,y)
    vertex(x+20,y-100+100*a1)
    vertex(x+60,y-100+100*a1)
    vertex(x+80-20*a1,y)
    vertex(x+119-59*a1,y)
    vertex(x-15+75*a1,y+150-150*a1)
    x=x-772
    vertex(x+30-30*a1,y+150-150*a1)
    endShape()
     # 下側に白ラインを引く
    stroke(255)
    strokeWeight(2)
    line(x-32,y-2,x+105-137*a1,y+149-151*a1)
    line(x+118,y-2,x+238-120*a1,y+149-151*a1)
    x=x+125
    line(x+79,y-1,x+178-99*a1,y+149-150*a1)
    x=x+155
    line(x-20,y-1,x+60-80*a1,y+149-150*a1)
    line(x+60,y-3,x+100-40*a1,y+149-152*a1)
    x=x+155
    line(x+160,y-1,x+120+40*a1,y+149-150*a1)
    x=x+57
    line(x+166,y-1,x+105+61*a1,y+149-150*a1)
    x=x+280
    line(x-59,y-1,x-145+86*a1,y+149-150*a1)
    line(x+81,y-1,x-50+131*a1,y+149-150*a1)

def nameC(x,y): #　真世界で赤く見える
     # 動きの軌跡
     # a4で座標がnameBと同様に変化
     # a4で徐々に用命になって消える
     # 影のみ描画する
     # kの頂点を設定
    x=x-380
    y=y-150
    stroke(255,0,0,120*a4)
    strokeWeight(5-5*a4)
    noFill()
    beginShape()
    vertex(x-30,y)
    vertex(x-100+70*a4,y+300)
    vertex(x-30,y+300)
    vertex(x,y+180+120*a4)
    vertex(x+50,y+300)
    vertex(x+120,y+300)
    vertex(x+30+27*a4,y+168+32*a4)
    vertex(x+80,y+120)
    vertex(x+120,y)
    vertex(x,y+96-96*a4)
    vertex(x+20,y)
    vertex(x-30,y)
    endShape()
     # Aの頂点を設定
    x=x+125
    beginShape()
    vertex(x,y)
    vertex(x-68,y+200)
    vertex(x,y+300)
    vertex(x,y+200+100*a4)
    vertex(x+45,y+200+100*a4)
    vertex(x+60,y+300)
    vertex(x+80,y+300)
    vertex(x+150,y)
    vertex(x,y)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(255,0,0,120*a4)
    beginShape()
    vertex(x,y+150-100*a4)
    vertex(x+50,y+150-100*a4)
    vertex(x+100,y+50)
    vertex(x+20,y+50)
    vertex(x,y+150-100*a4)
    endShape()
     # Mの頂点を設定
    x=x+155
    stroke(255,0,0,120*a4)
    noFill()
    beginShape()
    vertex(x,y)
    vertex(x-70,y+300)
    vertex(x-20,y+300)
    vertex(x+30,y+175+125*a4)
    vertex(x+60,y+300)
    vertex(x+110,y+175+125*a4)
    vertex(x+130,y+300)
    vertex(x+150,y+300)
    vertex(x+150,y-100+100*a4)
    vertex(x+75,y+100-100*a4)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+155
    beginShape()
    vertex(x,y+300)
    vertex(x+50,y+300)
    vertex(x+50,y+200+100*a4)
    vertex(x+120,y+200+100*a4)
    vertex(x+160,y+300)
    vertex(x+210,y+300)
    vertex(x,y-100+100*a4)
    vertex(x,y+300)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(255,0,0,120*a4)
    beginShape()
    vertex(x+50,y+150-100*a4)
    vertex(x+100-50*a4,y+150-100*a4)
    vertex(x+50,y+50)
    vertex(x+50,y+150-100*a4)
    endShape()
     # Tの頂点を設定
    x=x+57
    stroke(255,0,0,120*a4)
    noFill()
    beginShape()
    vertex(x-57*a4,y)
    vertex(x+40-57*a4,y+70)
    vertex(x+50-67*a4,y+70)
    vertex(x+165-57*a4,y+300)
    vertex(x+215+5*a4,y+300)
    vertex(x+140+140*a4,y+70)
    vertex(x+260+20*a4,y+70)
    vertex(x+275+5*a4,y)
    vertex(x-57*a4,y)
    endShape()
     # Aの頂点を設定
    x=x+280
    beginShape()
    vertex(x,y)
    vertex(x-60,y+300)
    vertex(x,y+300)
    vertex(x+20,y+200+100*a4)
    vertex(x+60,y+200+100*a4)
    vertex(x+80-20*a4,y+300)
    vertex(x+115-55*a4,y+300)
    vertex(x+60,y)
    vertex(x,y)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(255,0,0,120*a4)
    beginShape()
    vertex(x+25,y+150-100*a4)
    vertex(x+55,y+150-100*a4)
    vertex(x+45,y+50)
    vertex(x+20,y+50)
    vertex(x+25,y+150-100*a4)
    endShape()
     # Kの上側の影の頂点を設定
    x=x-772
    beginShape()
    vertex(x+60-60*a4,y+50-50*a4)
    vertex(x,y+96)
    vertex(x+22-22*a4,y-2+98*a4)
    endShape()
     # Kの右側の影の頂点を設定
    beginShape()
    vertex(x+30+53*a4,y+168-49*a4)
    vertex(x+83,y+119)
    x=x+125
    vertex(x-68+26*a4,y+203-84*a4)
    endShape()
     # Mの上側の影の頂点を設定
    x=x+155
    beginShape()
    vertex(x+82-82*a4,y+87-87*a4)
    vertex(x+75-75*a4,y+100-100*a4)
    vertex(x,y)
    endShape()
     # Kの下側の影の頂点を設定
    x=x-280
    y=y+300
    beginShape()
    vertex(x-104+74*a4,y)
    vertex(x-30,y)
    vertex(x,y-120+120*a4)
    vertex(x+50,y)
     # Aの影の頂点を設定
    x=x+125
    vertex(x,y)
    vertex(x,y-100+100*a4)
    vertex(x+45,y-100+100*a4)
    vertex(x+60,y)
     # Mの下側の影の頂点を設定
    x=x+155
    vertex(x-20,y)
    vertex(x+30,y-125+125*a4)
    vertex(x+60,y)
    vertex(x+110,y-125+125*a4)
    vertex(x+130,y)
     # Aの影の頂点を設定
    x=x+155
    vertex(x+50,y)
    vertex(x+50,y-100+100*a4)
    vertex(x+120,y-100+100*a4)
    vertex(x+160,y)
    vertex(x+210,y)
     # Tの影の頂点を設定
    x=x+57
    vertex(x-2+167*a4,y-300+300*a4)
    vertex(x+165*a4,y-300+300*a4)
    vertex(x+40+125*a4,y-230+230*a4)
    vertex(x+50+115*a4,y-230+230*a4)
    vertex(x+165,y)
    vertex(x+215,y)
    vertex(x+140,y-230+230*a4)
    vertex(x+260-45*a4,y-230+230*a4)
    vertex(x+275-55*a4,y-300+300*a4)
     # Aの影の頂点を設定
    x=x+280
    vertex(x,y-300+300*a4)
    vertex(x-60,y)
    vertex(x,y)
    vertex(x+20,y-100+100*a4)
    vertex(x+60,y-100+100*a4)
    vertex(x+80-20*a4,y)
    vertex(x+119-59*a4,y)
    vertex(x-15+75*a4,y+150-150*a4)
    x=x-772
    vertex(x+30-30*a4,y+150-150*a4)
    endShape()
     # 下側に赤ラインを引く
    stroke(255,0,0,120*a4)
    strokeWeight(2)
    line(x-32,y-2,x+105-137*a4,y+149-151*a4)
    line(x+118,y-2,x+238-120*a4,y+149-151*a4)
    x=x+125
    line(x+79,y-1,x+178-99*a4,y+149-150*a4)
    x=x+155
    line(x-20,y-1,x+60-80*a4,y+149-150*a4)
    line(x+60,y-3,x+100-40*a4,y+149-152*a4)
    x=x+155
    line(x+160,y-1,x+120+40*a4,y+149-150*a4)
    x=x+57
    line(x+166,y-1,x+105+61*a4,y+149-150*a4)
    x=x+280
    line(x-59,y-1,x-145+86*a4,y+149-150*a4)
    line(x+81,y-1,x-50+131*a4,y+149-150*a4)

def nameD(x,y): # 隠しコマンドで現れるやつ用のKAMATA
     # Kの頂点を設定
    x=x-380
    y=y-150
    stroke(0)
    strokeWeight(5)
    fill(255)
    beginShape()
    vertex(x-30,y)
    vertex(x-100,y+300)
    vertex(x-30,y+300)
    vertex(x,y+180)
    vertex(x+50,y+300)
    vertex(x+120,y+300)
    vertex(x+30,y+168)
    vertex(x+80,y+120)
    vertex(x+120,y)
    vertex(x,y+96)
    vertex(x+20,y)
    vertex(x-30,y)
    endShape()
     # Aの頂点を設定
    x=x+125
    beginShape()
    vertex(x,y)
    vertex(x-68,y+200)
    vertex(x,y+300)
    vertex(x,y+200)
    vertex(x+45,y+200)
    vertex(x+60,y+300)
    vertex(x+80,y+300)
    vertex(x+150,y)
    vertex(x,y)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(0)
    beginShape()
    vertex(x,y+150)
    vertex(x+50,y+150)
    vertex(x+100,y+50)
    vertex(x+20,y+50)
    vertex(x,y+150)
    endShape()
     # Mの頂点を設定
    x=x+155
    stroke(0)
    fill(255)
    beginShape()
    vertex(x,y)
    vertex(x-70,y+300)
    vertex(x-20,y+300)
    vertex(x+30,y+175)
    vertex(x+60,y+300)
    vertex(x+110,y+175)
    vertex(x+130,y+300)
    vertex(x+150,y+300)
    vertex(x+150,y-100)
    vertex(x+75,y+100)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+155
    beginShape()
    vertex(x,y+300)
    vertex(x+50,y+300)
    vertex(x+50,y+200)
    vertex(x+120,y+200)
    vertex(x+160,y+300)
    vertex(x+210,y+300)
    vertex(x,y-100)
    vertex(x,y+300)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(0)
    beginShape()
    vertex(x+50,y+150)
    vertex(x+100,y+150)
    vertex(x+50,y+50)
    vertex(x+50,y+150)
    endShape()
     # Tの頂点を設定
    x=x+57
    stroke(0)
    fill(255)
    beginShape()
    vertex(x,y)
    vertex(x+40,y+70)
    vertex(x+50,y+70)
    vertex(x+165,y+300)
    vertex(x+215,y+300)
    vertex(x+140,y+70)
    vertex(x+260,y+70)
    vertex(x+275,y)
    vertex(x,y)
    endShape()
     # Aの頂点を設定
    x=x+280
    beginShape()
    vertex(x,y)
    vertex(x-60,y+300)
    vertex(x,y+300)
    vertex(x+20,y+200)
    vertex(x+60,y+200)
    vertex(x+80,y+300)
    vertex(x+115,y+300)
    vertex(x+60,y)
    vertex(x,y)
    endShape()
     # Aの▲の頂点を設定
    noStroke()
    fill(0)
    beginShape()
    vertex(x+25,y+150)
    vertex(x+55,y+150)
    vertex(x+45,y+50)
    vertex(x+20,y+50)
    vertex(x+25,y+150)
    endShape()
     # Kの上側の影の頂点を設定
    x=x-772
    beginShape()
    vertex(x+60,y+50)
    vertex(x,y+96)
    vertex(x+22,y-2)
    endShape()
     # Kの右側の影の頂点を設定
    beginShape()
    vertex(x+30,y+168)
    vertex(x+83,y+119)
    x=x+125
    vertex(x-68,y+203)
    endShape()
     # Mの上側の影の頂点を設定
    x=x+155
    beginShape()
    vertex(x+82,y+87)
    vertex(x+75,y+100)
    vertex(x,y)
    endShape()
     # Kの下側の影の頂点を設定
    x=x-280
    y=y+300
    beginShape()
    vertex(x-104,y)
    vertex(x-30,y)
    vertex(x,y-120)
    vertex(x+50,y)
     # Aの影の頂点を設定
    x=x+125
    vertex(x,y)
    vertex(x,y-100)
    vertex(x+45,y-100)
    vertex(x+60,y)
     # Mの下側の影の頂点を設定
    x=x+155
    vertex(x-20,y)
    vertex(x+30,y-125)
    vertex(x+60,y)
    vertex(x+110,y-125)
    vertex(x+130,y)
     # Aの影の頂点を設定
    x=x+155
    vertex(x+50,y)
    vertex(x+50,y-100)
    vertex(x+120,y-100)
    vertex(x+160,y)
    vertex(x+210,y)
     # Tの影の頂点を設定
    x=x+57
    vertex(x-2,y-300)
    vertex(x,y-300)
    vertex(x+40,y-230)
    vertex(x+50,y-230)
    vertex(x+165,y)
    vertex(x+215,y)
    vertex(x+140,y-230)
    vertex(x+260,y-230)
    vertex(x+275,y-300)
     # Aの影の頂点を設定
    x=x+280
    vertex(x,y-300)
    vertex(x-60,y)
    vertex(x,y)
    vertex(x+20,y-100)
    vertex(x+60,y-100)
    vertex(x+80,y)
    vertex(x+119,y)
    vertex(x-15,y+150)
    x=x-772
    vertex(x+30,y+150)
    endShape()
     # 下側に白ラインを引く
    stroke(255)
    strokeWeight(2)
    line(x-32,y-2,x+105,y+149)
    line(x+118,y-2,x+238,y+149)
    x=x+125
    line(x+79,y-1,x+178,y+149)
    x=x+155
    line(x-20,y-1,x+60,y+149)
    line(x+60,y-3,x+100,y+149)
    x=x+155
    line(x+160,y-1,x+120,y+149)
    x=x+57
    line(x+166,y-1,x+105,y+149)
    x=x+280
    line(x-59,y-1,x-145,y+149)
    line(x+81,y-1,x-50,y+149)

def nameBOX(x,y): #KAMATAの名前が表示される前の箱
     # a1でKAMATAへ変化
     # KAMATAの各外側の頂点と箱の辺との距離の差分にa1をかけ
     # 時間経過で形が変わる
     # KAMATAの各外側の頂点の設定をする
    x=x-380
    y=y-150
    stroke(0)
    strokeWeight(5)
    fill(255)
    beginShape()
    vertex(x-30,y)
    vertex(x-100+70*a1,y+300)
    vertex(x-30,y+300)
    vertex(x,y+180+120*a1)
    vertex(x+50,y+300)
    vertex(x+120,y+300)
    x=x+125
    vertex(x,y+300)
    vertex(x,y+200+100*a1)
    vertex(x+45,y+200+100*a1)
    vertex(x+60,y+300)
    vertex(x+80,y+300)
    x=x+155
    vertex(x-70,y+300)
    vertex(x-20,y+300)
    vertex(x+30,y+175+125*a1)
    vertex(x+60,y+300)
    vertex(x+110,y+175+125*a1)
    vertex(x+130,y+300)
    vertex(x+150,y+300)
    x=x+155
    vertex(x,y+300)
    vertex(x+50,y+300)
    vertex(x+50,y+200+100*a1)
    vertex(x+120,y+200+100*a1)
    vertex(x+160,y+300)
    vertex(x+210,y+300)
    x=x+57
    x=x+280
    vertex(x-60,y+300)
    vertex(x,y+300)
    vertex(x+20,y+200+100*a1)
    vertex(x+60,y+200+100*a1)
    vertex(x+80-20*a1,y+300)
    vertex(x+115-55*a1,y+300)
    vertex(x+60,y)
    vertex(x,y)
    x=x-280
    vertex(x+275+5*a1,y)
    vertex(x-57*a1,y)
    x=x-57
    vertex(x+52.5-52.5*a1,y)
    vertex(x,y-100+100*a1)
    x=x-155
    vertex(x+150,y-100+100*a1)
    vertex(x+75,y+100-100*a1)
    vertex(x,y)
    x=x-155
    x=x-125
    vertex(x+120,y)
    vertex(x,y+96-96*a1)
    vertex(x+20,y)
    vertex(x-30,y)
    endShape()

def namaeA(x,y): # カマタを表示する
     # カのフの影の頂点を設定
    noStroke()
    x=x-300
    y=y+30+40
    noStroke
    fill(200,60,90,128) # 色を(200,60,90)透明度を128に設定
    beginShape()
    vertex(x,y+30)
    vertex(x+250,y-40)
    vertex(x+170,y+270)
    vertex(x+155,y+230)
    vertex(x+168,y+255)
    vertex(x+220,y-10)
    vertex(x+20,y+60)
    vertex(x+19,y+58.5)
    vertex(x+24,y+5)
    vertex(x+18,y+57)
    vertex(x+15,y+52.5)
    vertex(x+30,y+47)
    vertex(x+13,y+50)
    vertex(x+6,y+39)
    vertex(x+40,y+25)
    endShape()
     # カのノの影の頂点を設定
    beginShape()
    vertex(x+70,y-100)
    vertex(x+170,y-200)
    vertex(x+120,y+200)
    endShape()
    x=x+225
    y=y-90
    fill(200,60,90,128) # 色を(200,60,90)透明度を128に設定
     # マのフの影の頂点を設定
    beginShape()
    vertex(x-5,y-10)
    vertex(x+220,y-60)
    vertex(x+210,y-45)
    vertex(x+140,y+230)
    vertex(x+165,y-10)
    vertex(x+20,y+40)
    vertex(x-5,y-10)
    endShape()
     # マの＼の影の頂点を設定
    beginShape()
    vertex(x+100,y+140)
    vertex(x+190,y+230)
    vertex(x+165,y+215)
    vertex(x+200,y+240)
    vertex(x+160,y+220)
    vertex(x+230,y+270)
    vertex(x+110,y+210)
    endShape()
    x=x+260
    y=y-115
     # タのクの影の頂点を設定
    fill(200,60,90,128) # 色を(200,60,90)透明度を128に設定
    beginShape()
    vertex(x+40,y-10)
    vertex(x+190,y-70)
    vertex(x+180,y-60)
    vertex(x+100,y+365)
    vertex(x+140,y)
    vertex(x+77,y+30)
    vertex(x+10,y+160)
    vertex(x+13,y+120)
    vertex(x+3,y+150)
    vertex(x+5,y+130)
    vertex(x-1,y+140)
    vertex(x+1,y+125)
    vertex(x-15,y+150)
    vertex(x+40,y-10)
    endShape()
     # タの-の影の頂点を設定
    beginShape()
    vertex(x+35,y+60)
    vertex(x+150,y+40)
    vertex(x+140,y+70)
    vertex(x+10,y+120)
    endShape()
     # カのフの頂点を設定
    x=x-260
    y=y+115
    x=x-225
    y=y+90
    x=x-3
    y=y-3
    noStroke
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x,y+30)
    vertex(x+250,y-40)
    vertex(x+170,y+270)
    vertex(x+155,y+230)
    vertex(x+168,y+255)
    vertex(x+220,y-10)
    vertex(x+20,y+60)
    vertex(x+19,y+58.5)
    vertex(x+24,y+5)
    vertex(x+18,y+57)
    vertex(x+15,y+52.5)
    vertex(x+30,y+47)
    vertex(x+13,y+50)
    vertex(x+6,y+39)
    vertex(x+40,y+25)
    endShape()
     # カのノの頂点を設定
    beginShape()
    vertex(x+70,y-100)
    vertex(x+170,y-200)
    vertex(x+120,y+200)
    endShape()
     # マ
    x=x+225
    y=y-90
     # マのフ の頂点を設定
    x=x-3
    y=y-3
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x-5,y-10)
    vertex(x+220,y-60)
    vertex(x+210,y-45)
    vertex(x+140,y+230)
    vertex(x+165,y-10)
    vertex(x+20,y+40)
    vertex(x-5,y-10)
    endShape()
     # マの＼の頂点を設定
    beginShape()
    vertex(x+100,y+140)
    vertex(x+190,y+230)
    vertex(x+165,y+215)
    vertex(x+200,y+240)
    vertex(x+160,y+220)
    vertex(x+230,y+270)
    vertex(x+110,y+210)
    endShape()
     # タ
    x=x+260
    y=y-115
     # タのクの頂点を設定
    x=x-3
    y=y-3
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x+40,y-10)
    vertex(x+190,y-70)
    vertex(x+180,y-60)
    vertex(x+100,y+365)
    vertex(x+140,y)
    vertex(x+77,y+30)
    vertex(x+10,y+160)
    vertex(x+13,y+120)
    vertex(x+3,y+150)
    vertex(x+5,y+130)
    vertex(x-1,y+140)
    vertex(x+1,y+125)
    vertex(x-15,y+150)
    vertex(x+40,y-10)
    endShape()
     # タの-の頂点を設定
    beginShape()
    vertex(x+35,y+60)
    vertex(x+150,y+40)
    vertex(x+140,y+70)
    vertex(x+10,y+120)
    endShape()

def namaeB(x,y): # 隠しコマンドで現れるやつ用のカマタ
     # frameCountの増加によりsinも-1<=a<=1の間を単振動する
    a=sin(TWO_PI/80*frameCount)
     # frameCountの増加によりcosも-1<=b<=1の間を単振動する
    b=cos(TWO_PI/80*frameCount)
     # frameCountの増加によりtanも-∞<=c<=∞の間を振動する
    c=tan(PI/180*frameCount)
     # frameCountの増加によりcよりPI/12周期ずれてtanも-∞<=d<=∞の間を振動する
    d=tan(PI/180*frameCount+PI/12)
     # frameCountの増加によりdよりPI/12周期ずれてtanも-∞<=f<=∞の間を振動する
    e=tan(PI/180*frameCount+PI/6)
     # カのフの影の頂点を設定する
    x=(x-300)*a
    y=y+30+40*b
    noStroke()
    fill(20,170,40) # 色を(20,170,40)に設定
    beginShape()
    vertex(x,y+30*c)
    vertex(x+250*c,y-40*c)
    vertex(x+170*c,y+270*c)
    vertex(x+155*c,y+230*c)
    vertex(x+168*c,y+255*c)
    vertex(x+220*c,y-10*c)
    vertex(x+20*c,y+60*c)
    vertex(x+19*c,y+58.5*c)
    vertex(x+24*c,y+5*c)
    vertex(x+18*c,y+57*c)
    vertex(x+15*c,y+52.5*c)
    vertex(x+30*c,y+47*c)
    vertex(x+13*c,y+50*c)
    vertex(x+6*c,y+39*c)
    vertex(x+40*c,y+25*c)
    endShape()
     # カのノの影の頂点を設定する
    beginShape()
    vertex(x+70*c,y-100*c)
    vertex(x+170*c,y-200*c)
    vertex(x+120*c,y+200*c)
    endShape()
    x=x+225
    y=y-90
    fill(100,70,240) # 色を(100,70,240)に設定する
     # マのフの影の頂点を設定する
    beginShape()
    vertex(x-5*d,y-10*d)
    vertex(x+220*d,y-60*d)
    vertex(x+210*d,y-45*d)
    vertex(x+140*d,y+230*d)
    vertex(x+165*d,y-10*d)
    vertex(x+20*d,y+40*d)
    vertex(x-5*d,y-10*d)
    endShape()
     # マの＼の影の頂点を設定する
    beginShape()
    vertex(x+100*d,y+140*d)
    vertex(x+190*d,y+230*d)
    vertex(x+165*d,y+215*d)
    vertex(x+200*d,y+240*d)
    vertex(x+160*d,y+220*d)
    vertex(x+230*d,y+270*d)
    vertex(x+110*d,y+210*d)
    endShape()
    x=x+260
    y=y-115
     # タのクの影の頂点を設定する
    fill(255,200,140) # 色を(255,200,140)に設定する
    beginShape()
    vertex(x+40*e,y-10*e)
    vertex(x+190*e,y-70*e)
    vertex(x+180*e,y-60*e)
    vertex(x+100*e,y+365*e)
    vertex(x+140*e,y)
    vertex(x+77*e,y+30*e)
    vertex(x+10*e,y+160*e)
    vertex(x+13*e,y+120*e)
    vertex(x+3*e,y+150*e)
    vertex(x+5*e,y+130*e)
    vertex(x-1*e,y+140*e)
    vertex(x+1*e,y+125*e)
    vertex(x-15*e,y+150*e)
    vertex(x+40*e,y-10*e)
    endShape()
     # タの-の影の頂点を設定する
    beginShape()
    vertex(x+35*e,y+60*e)
    vertex(x+150*e,y+40*e)
    vertex(x+140*e,y+70*e)
    vertex(x+10*e,y+120*e)
    endShape()
     # カのフの頂点を設定する
    x=x-260
    y=y+115
    x=x-225
    y=y+90
    x=x-5
    y=y-5
    noStroke()
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x,y+30)
    vertex(x+250,y-40)
    vertex(x+170,y+270)
    vertex(x+155,y+230)
    vertex(x+168,y+255)
    vertex(x+220,y-10)
    vertex(x+20,y+60)
    vertex(x+19,y+58.5)
    vertex(x+24,y+5)
    vertex(x+18,y+57)
    vertex(x+15,y+52.5)
    vertex(x+30,y+47)
    vertex(x+13,y+50)
    vertex(x+6,y+39)
    vertex(x+40,y+25)
    endShape()
     # カのノの頂点を設定する
    beginShape()
    vertex(x+70,y-100)
    vertex(x+170,y-200)
    vertex(x+120,y+200)
    endShape()
     # マ
    x=x+225
    y=y-90
     # マのフの頂点を設定する
    x=x-5
    y=y-5
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x-5,y-10)
    vertex(x+220,y-60)
    vertex(x+210,y-45)
    vertex(x+140,y+230)
    vertex(x+165,y-10)
    vertex(x+20,y+40)
    vertex(x-5,y-10)
    endShape()
     # マの＼の頂点を設定する
    beginShape()
    vertex(x+100,y+140)
    vertex(x+190,y+230)
    vertex(x+165,y+215)
    vertex(x+200,y+240)
    vertex(x+160,y+220)
    vertex(x+230,y+270)
    vertex(x+110,y+210)
    endShape()
     # タ
    x=x+260
    y=y-115
     # タのクの頂点を設定する
    x=x-5
    y=y-5
    fill(255,80,10) # 色を(255,80,10)に設定
    beginShape()
    vertex(x+40,y-10)
    vertex(x+190,y-70)
    vertex(x+180,y-60)
    vertex(x+100,y+365)
    vertex(x+140,y)
    vertex(x+77,y+30)
    vertex(x+10,y+160)
    vertex(x+13,y+120)
    vertex(x+3,y+150)
    vertex(x+5,y+130)
    vertex(x-1,y+140)
    vertex(x+1,y+125)
    vertex(x-15,y+150)
    vertex(x+40,y-10)
    endShape()
     # タの-の頂点を設定する
    beginShape()
    vertex(x+35,y+60)
    vertex(x+150,y+40)
    vertex(x+140,y+70)
    vertex(x+10,y+120)
    endShape()

def king1(x,y): # 紫の太いラインが少し現れる
    for i in range(20): # iを20回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
        strokeWeight(2) # 線の太さを2に設定
         # 高さ120+i、横320-460に幅がランダムで変化する線を引く
        line(320-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),120+i,
             460+40*sin(PI/20*i*(random(1,10)/10)),120+i)
    for i in range(20): # iを20回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ126+i、横322-462に幅がランダムで変化する線を引く
        line(322-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),126+i,
             462+40*sin(PI/20*i*(random(1,10)/10)),126+i)
    for i in range(35): # iを35回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ400+i、横120-400に幅がランダムで変化する線を引く
        line(120-30*sin(PI/35*i*(random(1,10)/10)),400+i,
             400+40*sin(PI/35*i*(random(1,10)/10)),400+i)
    for i in range(35): # iを35回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ406+i、横122-402に幅がランダムで変化する線を引く
        line(122-30*sin(PI/45*i*(random(1,10)/10)),406+i,
             402+40*sin(PI/45*i*(random(1,10)/10)),406+i)
    for i in range(35): # iを35回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ230+i、横720-1100に幅がランダムで変化する線を引く
        line(720-30*sin(PI/35*i*(random(1,10)/10)),230+i,
             1100+40*sin(PI/35*i*(random(1,10)/10)),230+i)
    for i in range(35): # iを35回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ236+i、横722-1102に幅がランダムで変化する線を引く
        line(722-30*sin(PI/45*i*(random(1,10)/10)),236+i,
             1102+40*sin(PI/45*i*(random(1,10)/10)),236+i)
    for i in range(55): # iを55回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ510+i、横520-920に幅がランダムで変化する線を引く
        line(520-30*sin(PI/35*i*(random(1,10)/10)),510+i,
             920+40*sin(PI/35*i*(random(1,10)/10)),510+i)
    for i in range(55): # iを55回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ516+i、横522-922に幅がランダムで変化する線を引く
        line(522-30*sin(PI/45*i*(random(1,10)/10)),516+i,
             922+40*sin(PI/45*i*(random(1,10)/10)),516+i)

def king2(x,y): # 紫の太いラインが現れる
    for i in range(12): # iを12回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
        strokeWeight(2) # 線の太さを2に設定
         # 高さ120+i、横200-360に幅がランダムで変化する線を引く
        line(200-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),120+i,
             360+40*sin(PI/20*i*(random(1,10)/10)),120+i)
    for i in range(12): # iを12回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ126+i、横202-362に幅がランダムで変化する線を引く
        line(202-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),126+i,
             362+40*sin(PI/20*i*(random(1,10)/10)),126+i)
    for i in range(55): # iを55回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ400+i、横820-1280に幅がランダムで変化する線を引く
        line(820-30*sin(PI/35*i*(random(1,10)/10)),400+i,
             1280+40*sin(PI/35*i*(random(1,10)/10)),400+i)
    for i in range(55): # iを55回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ406+i、横822-1282に幅がランダムで変化する線を引く
        line(822-30*sin(PI/45*i*(random(1,10)/10)),406+i,
             1282+40*sin(PI/45*i*(random(1,10)/10)),406+i)
    for i in range(25): # iを25回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ200+i、横720-1300に幅がランダムで変化する線を引く
        line(720-30*sin(PI/35*i*(random(1,10)/10)),200+i,
             1300+40*sin(PI/35*i*(random(1,10)/10)),200+i)
    for i in range(25): # iを25回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ206+i、横722-1302に幅がランダムで変化する線を引く
        line(722-30*sin(PI/45*i*(random(1,10)/10)),206+i,
             1302+40*sin(PI/45*i*(random(1,10)/10)),206+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ310+i、横0-920に幅がランダムで変化する線を引く
        line(0-30*sin(PI/35*i*(random(1,10)/10)),310+i,
             920+40*sin(PI/35*i*(random(1,10)/10)),310+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ316+i、横0-922に幅がランダムで変化する線を引く
        line(0-30*sin(PI/45*i*(random(1,10)/10)),316+i,
             922+40*sin(PI/45*i*(random(1,10)/10)),316+i)
    for i in range(15): # iを15回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ630+i、横0-770に幅がランダムで変化する線を引く
        line(0-30*sin(PI/35*i*(random(1,10)/10)),630+i,
             770+40*sin(PI/35*i*(random(1,10)/10)),630+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ636+i、横0-772に幅がランダムで変化する線を引く
        line(0-30*sin(PI/45*i*(random(1,10)/10)),636+i,
             772+40*sin(PI/45*i*(random(1,10)/10)),636+i)
    for i in range(10): # iを10回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ270+i、横520-1300に幅がランダムで変化する線を引く
        line(520-30*sin(PI/35*i*(random(1,10)/10)),270+i,
             1300+40*sin(PI/35*i*(random(1,10)/10)),270+i)
    for i in range(10):  # iを10回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ276+i、横522-1302に幅がランダムで変化する線を引く
        line(522-30*sin(PI/45*i*(random(1,10)/10)),276+i,
             1302+40*sin(PI/45*i*(random(1,10)/10)),276+i)

def king3(x,y): # 紫の太いラインがたくさん現れる
    for i in range(60): # iを60回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
        strokeWeight(2) # 線の太さを2に設定
         # 高さ30+i、横10-660に幅がランダムで変化する線を引く
        line(10-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),30+i,
             660+40*sin(PI/20*i*(random(1,10)/10)),30+i)
    for i in range(60): # iを60回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ36+i、横12-662に幅がランダムで変化する線を引く
        line(12-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),36+i,
             662+40*sin(PI/20*i*(random(1,10)/10)),36+i)
    for i in range(30): # iを30回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ10+i、横710-1360に幅がランダムで変化する線を引く
        line(710-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),10+i,
             1360+40*sin(PI/20*i*(random(1,10)/10)),10+i)
    for i in range(30): # iを30回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ16+i、横712-1362に幅がランダムで変化する線を引く
        line(712-30*sin(PI/20*i*random(1,2))*sin(PI/20*i*random(1,2)),16+i,
             1362+40*sin(PI/20*i*(random(1,10)/10)),16+i)
    for i in range(40): # iを40回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ400+i、横120-1280に幅がランダムで変化する線を引く
        line(120-30*sin(PI/35*i*(random(1,10)/10)),400+i,
             1280+40*sin(PI/35*i*(random(1,10)/10)),400+i)
    for i in range(40): # iを40回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ406+i、横122-1280に幅がランダムで変化する線を引く
        line(122-30*sin(PI/45*i*(random(1,10)/10)),406+i,
             1282+40*sin(PI/45*i*(random(1,10)/10)),406+i)
    for i in range(25):  # iを25回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ200+i、横470-1300に幅がランダムで変化する線を引く
        line(470-30*sin(PI/35*i*(random(1,10)/10)),200+i,
             1300+40*sin(PI/35*i*(random(1,10)/10)),200+i)
    for i in range(25): # iを25回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ206+i、横472-1302に幅がランダムで変化する線を引く
        line(472-30*sin(PI/45*i*(random(1,10)/10)),206+i,
             1302+40*sin(PI/45*i*(random(1,10)/10)),206+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ310+i、横0-920に幅がランダムで変化する線を引く
        line(0-30*sin(PI/35*i*(random(1,10)/10)),310+i,
             920+40*sin(PI/35*i*(random(1,10)/10)),310+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ316+i、横0-922に幅がランダムで変化する線を引く
        line(0-30*sin(PI/45*i*(random(1,10)/10)),316+i,
             922+40*sin(PI/45*i*(random(1,10)/10)),316+i)
    for i in range(15): # iを15回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ630+i、横0-1170に幅がランダムで変化する線を引く
        line(0-30*sin(PI/35*i*(random(1,10)/10)),630+i,
             1170+40*sin(PI/35*i*(random(1,10)/10)),630+i)
    for i in range(45): # iを45回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ636+i、横0-1172に幅がランダムで変化する線を引く
        line(0-30*sin(PI/45*i*(random(1,10)/10)),636+i,
             1172+40*sin(PI/45*i*(random(1,10)/10)),636+i)
    for i in range(10): # iを10回繰り返す
         # 線の色をランダムな濃い青に透明度を50-100の間でランダムに設定
        stroke(0,random(0,51),204+random(0,51),random(50,100))
         # 高さ270+i、横220-1300に幅がランダムで変化する線を引く
        line(220-30*sin(PI/35*i*(random(1,10)/10)),270+i,
             1300+40*sin(PI/35*i*(random(1,10)/10)),270+i)
    for i in range(10): # iを10回繰り返す
         # 線の色をランダムな紫に透明度を100-160の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(100,160))
         # 高さ276+i、横222-1302に幅がランダムで変化する線を引く
        line(222-30*sin(PI/45*i*(random(1,10)/10)),276+i,
             1302+40*sin(PI/45*i*(random(1,10)/10)),276+i)

def king4(x,y): # 背景が紫に染まる
    for i in range(180): # iを180回繰り返す
        strokeWeight(4) # 線の太さを4に設定
         # 線の色をランダムな紫に透明度を60-110の間でランダムに設定
        stroke(204,random(0,51),204+random(0,51),random(60,110))
         # 高さ4*i、横0-widthに幅がランダムで変化する線を引く
        line(0+20*sin(PI/45*i*(random(1,10)/10)),4*i,
             width+20*sin(PI/45*i*(random(1,10)/10)),4*i)

def hukitobu(x,y): # 演出のために消し飛ぶかわいそうな背景
     # 各四角形が3つに割れて画面外へ消し飛ぶ
     # a2が変化して座標が変化する
     # 赤い四角形の頂点を設定
    noStroke()
    fill(255,128,128) # 色を(255,128,128)に設定
    beginShape()
    vertex(x-643-200*a2,y-363-140*a2)
    vertex(x-340-320*a2,y-363-180*a2)
    vertex(x-340-300*a2,y-241-120*a2)
    vertex(x-643-100*a2,y-181-300*a2)
    endShape()
    beginShape()
    vertex(x-643-100*a2,y-175+20*a2)
    vertex(x-340-700*a2,y-239+240*a2)
    vertex(x-340-600*a2,y-2-200*a2)
    vertex(x-643-50*a2,y+58-120*a2)
    endShape()
    beginShape()
    vertex(x-643-115*a2,y+64+20*a2)
    vertex(x-340-320*a2,y+30*a2)
    vertex(x-340-450*a2*a2,y+60+530*a2)
    endShape()
    #緑の四角形の頂点を設定
    fill(128,255,128) # 色を(128,255,128)に設定
    beginShape()
    vertex(x-643-115*a2,y+60+420*a2)
    vertex(x-340-450*a2*a2,y+60+500*a2)
    vertex(x-643-25*a2,y+363+60*a2)
    endShape()
    beginShape()
    vertex(x-337+30*a2,y+60+400*a2)
    vertex(x+58-40*a2,y+60+500*a2)
    vertex(x-246+80*a2,y+363+20*a2)
    vertex(x-633-90*a2,y+363+30*a2)
    endShape()
    beginShape()
    vertex(x+61+70*a2,y+60+360*a2)
    vertex(x+334+50*a2,y+60+320*a2)
    vertex(x+340+60*a2,y+363+40*a2)
    vertex(x-232+300*a2,y+363+40*a2)
    endShape()
     # 青い四角形の頂点を設定
    fill(0,128,255) # 色を(0,128,255)に設定
    beginShape()
    vertex(x+643+300*a2,y+363+60*a2)
    vertex(x+346+500*a2,y+363+20*a2)
    vertex(x+340+475*a2,y+248+60*a2)
    vertex(x+643+100*a2,y+181+100*a2)
    endShape()
    beginShape()
    vertex(x+643+20*a2,y+178+250*a2)
    vertex(x+340+600*a2,y+236-70*a2)
    vertex(x+340+740*a2,y-2+70*a2*a2)
    vertex(x+643+30*a2,y+60-130*a2)
    endShape()
    beginShape()
    vertex(x+643+300*a2,y-54+30*a2)
    vertex(x+643+190*a2,y+58+40*a2)
    vertex(x+340+460*a2,y-7+40*a2)
    vertex(x+340+380*a2,y-56+20*a2)
    endShape()
     # 黄色い四角形の頂点を設定
    fill(255,255,130) # 色を(255,255,130)に設定
    beginShape()
    vertex(x+643+50*a2,y-57-40*a2)
    vertex(x+349+500*a2,y-60-400*a2)
    vertex(x+643+30*a2,y-363-75*a2)
    endShape()
    beginShape()
    vertex(x+342-60*a2,y-60-380*a2)
    vertex(x-46+125*a2,y-60-444*a2)
    vertex(x+244+100*a2,y-363-130*a2)
    vertex(x+643-200*a2,y-363-90*a2)
    endShape()
    beginShape()
    vertex(x-55-300*a2,y-60-400*a2)
    vertex(x-333+100*a2,y-60-495*a2)
    vertex(x-338+200*a2,y-363-30*a2)
    vertex(x+240-500*a2,y-363-60*a2)
    endShape()
    
def hosi(x,y): # 背景が消し飛ぶと宇宙が現れる
     # 1で小さい星、2で大きい星、0は何も表示しない
    listHosi=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
              0,0,1,0,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
              0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,
              0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
              0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
              0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,
              1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    for i in range(800): # iを800回繰り返す
         # もしlistHosiのi番目が1ならば
        if listHosi[i]==1:
            noStroke()   # 縁を描画しない
             # 色をランダムな紫に、透明度を90-190でランダムに設定する
            fill(204,0,102,random(90,190))
             # 円のx方向の間隔・y方向の間隔を40、縦幅・横幅を7-13でランダムに設定する
             # i番目の円を(x+i%40*40,y+i/40*40)に描画
            ellipse(x+i%40*40,y+i/40*40,random(7,13),random(7,13))
             # 色を(255,220,220)に設定
            fill(255,220,220)
             # 円のx方向の間隔・y方向の間隔を40、縦幅・横幅を4に設定する
             # i番目の円を(x+i%40*40,y+i/40*40)に描画
            ellipse(x+i%40*40,y+i/40*40,4,4)
         # もしlistHosiのi番目が2ならば
        elif listHosi[i]==2:
            noStroke()    # 線を描画しない
             # 色をランダムな紫に、透明度を90-190でランダムに設定する
            fill(204,0,102,random(90,190))
             # 円のx方向の間隔・y方向の間隔を40、縦幅・横幅を10-18でランダムに設定する
             # i番目の円を(x+i%40*40,y+i/40*40)に描画
            ellipse(x+i%40*40,y+i/40*40,random(10,18),random(10,18))
             # 色を(255,220,220)に設定
            fill(255,220,220)
             # 円のx方向の間隔・y方向の間隔を40、縦幅・横幅を4に設定する
             # i番目の円を(x+i%40*40,y+i/40*40)に描画
            ellipse(x+i%40*40,y+i/40*40,10,10)
