import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://3.bp.blogspot.com/-927kUoBsyqo/U-8HFxT4xsI/AAAAAAAAk_I/pUjTeBXsS7A/s800/job_ekisya.png'
YOUR_ICON = 'https://1.bp.blogspot.com/-Fn-oz-1cGTI/X4aVjdBGL0I/AAAAAAABbwY/bG-apG9Dk9AtYWlGuiqSc9N8A-l5Z7XAwCNcBGAsYHQ/s400/hamster_sleeping_golden.png'

def run_chat(chat = chat, start='占いするよ', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', '占い師')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

#ソウルナンバー関数
def soulnumber(s):
  while True:
    l=len(s)
    if l==1:
      return s
    elif l==2:
      if s[0]==s[1]:
        return s
      else:
        s=str(sum(int(x) for x in s))
    else:
      s=str(sum(int(x) for x in s))
 
#誕生日のナンバー計算
def birthdaynumber(birthday):
  birthdaynumber=soulnumber(birthday)
  return birthdaynumber

#今日のソウルナンバー計算
def todaynumber():
  import datetime
  dt=datetime.datetime.today()
  today=str(dt.year)+str(dt.month)+str(dt.day)
  num2=soulnumber(today)
  return num2 

def uranai(birthday):
  #誕生日ナンバー
  number1=birthdaynumber(birthday)
  #今日のナンバー
  number2=todaynumber()
  #計算
  number=int(soulnumber(number1+number2))
  #結果
  if number==0:
    memo="今日の運勢は凶です!"
  elif number<=5:
    memo="今日の運勢は吉です!"
  elif number<=9:
    memo="今日の運勢は大吉です!"
  else:
    memo="今日は最高な１日になるでしょう!!"
  return memo

#ポジティブな言葉
import random
def positive(type):
  L1=["不安や迷いがあっても","どんな壁にぶつかっても","どんなにつらくても","最後の最後まで"]
  L2=["諦めない","やってみる","自分を信じる","笑えばいい","前へ進む"
    ,"がむしゃらに","見失わない","挑戦する","一歩踏み出す","立ち上がる"]
  RANDOM=random.randint(0,9)
  if type=="A":
    return L1[0]+L2[RANDOM]
  elif type=="B":
    return L1[1]+L2[RANDOM]
  elif type=="O":
    return L1[2]+L2[RANDOM]
  else:
    return L1[3]+L2[RANDOM]
  
#誕生日入力
import re
pattern = r'(\d\d\d\d)\D(\d\d?)\D(\d\d?)'
pattern = re.compile(pattern)

def P1(input_text):
  try:
    input=input_text.strip()
    input=pattern.findall(input)
    birthday= ''.join(*input)
  except:
    birthday=input_text.strip()
  return birthday

#YES/NO
def P2(input_text):
  input=input_text.strip()
  Y=["YES","はい","うん","きく"]
  if input in Y:
    ans="YES"
  else:
    ans="NO"
  return ans

#血液型
def P3(input_text):
  input=input_text
  if "AB" in input:
    type="AB"
  elif "A" in input:
    type="A"
  elif "B" in input:
    type="B"
  else:
    type="O"
  return type

n = 0 # 状態 (関数の外側)

def mychat2(input_text, **kw):  #チャット用の関数
  global n
  n += 1
  
  if n==1:
    text="あなたの誕生日は？"
  elif n==2:
    birthday=P1(input_text)
    text=uranai(birthday)+"今日の一言聞きますか?"
  elif n==3:
    ans=P2(input_text)
    if ans=="YES":
      text="あなたの血液型は？"
    else:
      text="ご利用ありがとうございました！"
      n=0
  elif n==4:
    type=P3(input_text)
    text=positive(type)
  else:
    text="ご利用ありがとうございました！"
    n=0
  return text

def start():
  run_chat(chat=mychat2)#関数名を渡します

 
