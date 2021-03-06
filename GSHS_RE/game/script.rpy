#캐릭터 일러스트
init:
    image 정은하 스탠딩 = "Character/정은하_스탠딩.png"
    image 정은하 신남 = "Character/정은하_신남.png"
    image 정은하 짜증 = "Character/정은하_짜증.png"
    image 정은하 휴대폰 = "Character/정은하_휴대폰.png"
    image 한지아 스탠딩 = "Character/한지아_스탠딩.png"
    image 채나연 스탠딩 = "Character/채나연_스탠딩.png"
    image 채나연 땀 = "Character/채나연_땀.png"
    image 채나연 부끄 = "Character/채나연_부끄.png"
    image 채나연 화남 = "Character/채나연_화남.png"
    image 채나연 웃음 = "Character/채나연_웃음.png"

#캐릭터 선언
init:
    #캐릭터 이름으로 수정함
    define 은하 = Character("정은하")
    define 재영 = Character("김재영")
    define 지아 = Character("한지아")
    define 나연 = Character("채나연")
    define 학생_1 = Character("지나가던 학생")
    define Unknown = Character("???")
    define 나레이터 = nvl_narrator

#배경
init:
    image 검은화면 = "검은화면.png"
    image 밤하늘 = "밤하늘.png"
    image 재영방_day = "재영방_day.jpg"
    image 재영방_night = "재영방_night.jpg"
    image 통학로 = "통학로.jpg"
    image 통학로2 = "통학로2.jpg"
    image 교문 = "학교배경/교문.jpg"
    image 신발장 = "학교배경/신발장.jpg"
    image 교실 = "학교배경/교실_2.jpg"
    image 동아리실 = "동아리실.jpg"
    image 남주집_night = "남주집_night.jpg"
    image 선택화면_선택이전 = "선택화면_선택이전.png"
    image 선택화면_선택 = "선택화면_선택.png"
    image 번화가 = "번화가.jpg"

init python:
    style.default.language = "korean-with-spaces"

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
            time,
            child,
            add_sizes=True,
            **properties)

        Shake = renpy.curry(_Shake)
    #

#
screen character_select_Screen:

    imagemap:
        #these are your images
        idle "선택화면_선택이전"
        hover "선택화면_선택"
        #these are your hotspots, alter them to fit your screen and however you want it to look. Add one every time you create a new point.
        hotspot (0, 0, 640, 1080) action SetVariable("character_select", 1), Return()
        hotspot (640, 0, 640, 1080) action SetVariable("character_select", 2), Return()
        hotspot (1280, 0, 640, 1080) action SetVariable("character_select", 3), Return()


# 여기에서부터 게임이 시작합니다.
label start:
    $character_select = 0 # 1 정은하, 2 채나연, 3 한지아

    play music "audio/첫부분 밤하늘곡.mp3"

    #scene 이 없음, 그저 검은화면임

    "깊은 꿈이었을 것이다."
 
    "스스로에게 화가 나 입술을 짓씹었고"

    "안타까움에 애꿎은 땅을 괴롭히듯 즈려밟았다."

    "내가 알았더라면, {w}좀 더 이해했더라면, {w}좀 더 시간이 있었다면." 


    "이런 의미없는 후회들은 흐르듯이, 자연스레 조각들과 함께 했다."

    "이미 지나가버리고 흩어져버린 의미들을 주워담기엔\n{w}그것들은 색이 바래, 흐린 안개와 같았다."

    "고개를 들었다.\n{w}앞을 보기엔 무서웠고 밑을 보기엔 죄책감이 들어 무작정 위를 보았다."

    #여기서부터 scene 밤하늘 시작

    scene 밤하늘
    with fade

    "평소엔 그저 예쁘게만 보이던 별빛들이"

    "지금은 달빛이 아스러진 조각들 같아 보인다."

    "그 빛을 보며 문득 그런 생각이 들었다."

    "내가 하려던 것은 저 별빛들을 다시 모아 달로 만드려던 것은 아니었을까"

    "감당하지 못할 것을 알면서도 정면으로 부닥쳐 온 나는 그저 주제파악 못 한 어린 아이가 아니었을까."

    "힘이 풀리는 듯 했다."

    "나의 선택이 틀렸다고 믿고싶지 않았지만"

    "나는 그걸 받아들여야했다."

    "싫었다. {w}그저 피하고 싶었다."

    "별빛들이 짜증났다."

    "짜증나니까. 싫으니까. 피하고 싶으니까"

    "눈꺼풀로 황급히 눈을 가리듯 질끈 눈을 감고."

    "짜증나는 별빛을 보지 않도록 가만히 서서 다시 아침이 오길 기다렸다."

label 첫날_아침_정은하_첫만남:

    scene 재영방_day
    with fade
    play music "audio/대화할때 기본곡.mp3"

    은하 "재영~! 일어나!!"

    "조용하기만 하던 방안에 울리는 쨍한 소리에 무심코 인상을 찡그렸다."

    "몽롱한 기운을 지우지 못한 채 베개에 더 깊게 얼굴을 파묻으며 몸을 뒤척였다."

    "이불과 온 몸을 밀착한 채 끈질기게 붙어있던 눈꺼풀을 살짝 들어올리니, 서있던 은하의 모습이 눈에 들어왔다."

    show 정은하 스탠딩
    with dissolve
    
    은하 "김재영! 우리 지금 지각이야! 얼른 씻고 준비해!"

    "은하는 덤덤히 자기 할 말만 하고 방 문을 닫고 계단 밑으로 내려갔다."

    hide 정은하 스탠딩
    with dissolve

    "멍하니 은하가 사라진 자리를 물끄러미 바라보며 자그마한 헛웃음을 흘렸다."

    "소꿉친구라고 해도 이렇게 남자 방에 당당히 들어오는 상황이 처음엔 뻘쭘했지만 이게 몇년이 되다보니 익숙해져버렸다."

    "익숙해지는게 맞는 건가 싶은 고민을 흘리며 지각을 면하기 위해 간단한 세면도구를 챙긴 뒤 욕실로 향했다."

label 첫날_학교:
    
    scene 통학로
    with fade

    show 정은하 스탠딩
    with dissolve

    은하 "아! 재영아, 너네 부모님 언제 다시 오신다고 했지?"

    재영 "음...아마 내년 쯤엔 오시지않을까? 바쁘셔도 항상 새해는 같이 보냈으니까."

    "초등학교 중학교 때까지는 가족과 함께 이곳에서 지냈지만 고등학교를 들어오고 나서는 일 때문에 부모님 모두 멀리 떨어져 지내는 상태이다."

    "은하와 내가 어릴 적부터 친해서인지 예전부터 아무 거부감없이 내 집에 자주 놀러왔고 부모님도 은하를 딸처럼 대해주셨다."

    "지금은 부모님이 멀리 계시니 은하에게 자기들 대신 나를 부탁한다는 말도 했었는데."

    "…..이렇게 방에 들어오기까지 할 줄은 몰랐다."

    "여유롭게 걸어가던 은하는 교문에 다다르자 고개를 급히 돌려 나를 바라보고선 다급하게 외쳤다."

    은하 "재영아 뛰어뛰어!!! 이러다가 선도부한테 걸리겠다!"

    "은하는 다급한 한마디를 던짐과 동시에 뛰기 시작했다. {w} 이미….늦은 것 같지만."

    hide 정은하 스탠딩

label 첫날_교문_한지아_첫만남:

    scene 교문
    with fade

    show 한지아_스탠딩
    with dissolve
    
    지아 "너넨 벌점이야."

    "뜀박질이 무의미하게 이미 문 앞을 막고 있는 한 소녀가 보였다."

    "긴 흑발에 안경을 써서 차분한 인상을 주는 소녀는 담담히 벌점기록부에 우리의 이름을 적어내리고 있었다."

    지아 "지각 벌점 1점이야."

    지아 "새학기 초반부터 지각이라니. 다른 1학년도 배짱좋게 지각이던데 다들 학교생활 편한가봐?"

    "한 쪽 눈꼬리를 올리며 우리에게 묻듯이 질문하는 학생회장은 우리를 흘끗 한 번 보고는 다른 학생이 있는 쪽으로 고개를 돌렸다."

    지아 "뭘 왜긴 왜야. 그게 규정이니까 그렇지."

    학생_1 "치사해! 야박해! 마녀!!!" with Shake((0,0,0,0),1.0,dist=5)

    지아 ".....벌점 1점 추가."

    학생_1 "안돼애애~!!!"
    

    "괜히 말을 덧붙이다가 벌점만 더 받아버린 그 1학년은 발을 동동 구르며 분한 마음에 학생회장을 노려보다가 이내 지쳤는지 바닥에 털썩 주저앉았다."

    "그런 모습을 한심하게 바라보던 학생회장은 가벼운 한숨을 내쉬며 이젠 우리에겐 볼 일이 없다는 듯 손짓으로 우리 둘을 교문 안쪽으로 보내주었다."

    hide 한지아

    scene 신발장
    with fade

    show 정은하 스탠딩
    with dissolve
    
    은하 "우와… 학생회장님 무섭네."

    "은하는 안도의 숨을 뱉으며 좀 더 가벼워진 발걸음으로 교실로 향했다."

    hide 정은하

    재영 "그러게, 앞으로 좀 조심해야겠어."

    "귀찮은 일이 생기는 것은 질색이기에 학생회장과는 엮이지 말자는 작은 다짐을 하고 학생회장의 옆모습을 흘끗 보았다."

    재영 ".....?"

    "평소였으면 무섭게 보일 터인 학생회장의 얼굴이 갑작스레 오늘따라 다르게 느껴진다는 생각을 잠시 하다가 금방 정신을 차리고 은하의 발걸음에 맞춰 천천히 계단을 올랐다."

label 첫날_점심시간:

    scene 교실
    with fade

    "오전 수업이 끝난 후 점심시간"
    "교실이 한층 더 떠들썩해졌다."
    "아마 오전에 선생님께서 동아리가입에 대한 공지를 한 것에 대한 말들이 오가는 듯 했다."
    "다들 자기의 흥미에 맞는 동아리를 고르며 즐거워하는 와중에 나는 그저 멍하니 동아리 리스트가 적힌 유인물을 바라보고 있었다."
    
    show 정은하 스탠딩
    with dissolve

    은하 "그래서 재영, 넌 어디 갈건데?"

    "같은 반 앞자리에 앉아있던 은하가 뒤로 돌아 나에게 물었다."

    재영 "동아리를 꼭 들어가야할까."

    "솔직히 동아리에 들어갈 이유가 없었다."

    "그도 그럴 것이 딱히 내 취미라고 할 것도 없고 특출난 장점 또한 없었다."

    "딱히 의미를 두지 않고 던진 말에 은하는 가만히 고민하더니 이걸 뭐라 설명해줘야 될지 모르겠다는 표정으로 대답했다."

    은하 "음...뭐 가면 친구 사귀고 좋지?"

    재영 "귀찮은데…."

    은하 "여자 부원이랑 친해질 수도 있고?"

    재영 "동아리는 좋은 곳이었구나. 어디 갈까?"

    은하 "....으이구."

    "은하는 질색이라는 표정을 짓더니 이내 진지하게 내가 들어갈 동아리를 같이 고민해 주었다."

    은하 "난 댄스 동아리 들어가려구. 예전부터 들어가보고 싶었거든."

    은하 "재영이 넌….게임 좋아하니까 게임동아리…? 좀 별로려나?"

    "불호가 확실한 편인 은하와 달리 난 딱히 어느 동아리든 상관이 없었다."

    "그저 귀찮지 않고 적당히 인맥만 쌓을 정도면 되었다."

    "그런 상태에서 내가 고를 만한 동아리는 한 개밖에 없었다."

    재영 "난 여기로 하려고."

    hide 정은하

label 첫날_동아리실_채나연_첫만남:

    scene 동아리실
    with fade

    play music "audio/동아리실음악.mp3"

    "무작정 신청서만 낼 작정이었던 나는 동아리장의 허락을 맡아야된다는 선생님의 말을 듣고선 어쩔 수 없이 동아리실에 찾아갔다."

    "전혀 예상치 못한 상황이었지만 뭐 어쩌겠는가."

    재영 "누구….계신가요~?"

    "무작정 동아리 신청서를 들고 동아리실로 향하고는 안에 사람이 있는지 확인했다."

    stop music fadeout 2.0

    "시끌벅적 할 것 같았던 예상과 달리 동아리실엔 침묵만 감돌았다."

    "손에 들려있는 신청서를 다시금 의식하며 동아리실 안쪽으로 조금씩 발을 내딛었다."

    "내딛는 발에 맞춰 바닥의 나무 타일에서 세월이 느껴지는 삐그덕 소리가 났고"

    play sound "audio/삐그덕소리.mp3"

    "삐그덕 거리는 소리는 적막한 동아리실을 가득 채우기에 충분했다."

    "동아리실을 채우던 소리가 익숙해져서 일정한 박자로 들릴 때 쯔음"

    play music "audio/동아리실음악.mp3"

    show 채나연 스탠딩
    with dissolve

    Unknown "너 뭐야?"

    "뒤쪽에서 무심하면서도 궁금증 어린 목소리가 들려왔다."

    "조용한 곳이어서 그런지 아까의 삐그덕 소리가 기억이 나지 않을 정도로 선명히 들려왔다."

    재영 "아….누구세요?"

    "순간 당황해서 아무말을 내뱉어 버렸다."

    Unknown "...?"

    "그 목소리의 주인은 이게 무슨 말인가 싶어 잠시 인상을 찌푸리다 이내 내가 들고있던 종이를 슬쩍 보더니 무슨 상황인지 알겠다는 듯 나에게 물었다."

    Unknown "신입생이구나?"

    재영 "네..."

    Unknown "그건 동아리 가입 신청서?"

    재영 "네에...그렇죠?"

    Unknown "줘 봐."

    "그리말하고는 자연스래 내 종이를 빼앗아서 빠르게 훑어보더니 한 마디를 툭 던졌다."

    Unknown "왜?"

    재영 "예?"

    Unknown "왜 여기에 가입하려고 하냐고."

    재영 "아….."

    "딱히 할 말이 없었다."

    "동아리 가입은 해야겠는데 조용한 활동을 하고 싶고 동아리시간에 각자 공부할 시간을 주거나 별 활동을 안 할것 같았던 동아리가 딱 여기 ‘역사문화탐구 동아리’였는데."

    "그 말을 어떻게 부원처럼 보이는 사람 앞에서 하겠냐고!"

    "그렇게 대답을 망설이던 중 말을 꺼낸 장본인은 대답이 궁금하지 않다는 듯 자그마한 웃음을 흘리고는 빠르게 종이에 싸인을 써갈겼다."

    Unknown "자 여기. 김재영이라고 했지?"

    재영 "네. 근데 싸인….해주신거면 동아리장이신가요?"

    Unknown "그래. 그래봤자 유령동아리여서 활동은 거의 없어. 동아리방 쓰고 싶을 때면 써. 조용해서 공부하기는 좋거든."

    "말을 마치고서는 이젠 볼일 끝났다는 듯.\n 동아리장은 읽고있던 책을 다시 집어들고 나를 신경쓰지 않은 채 읽기 시작하였다."

    "나는 아무래도 상관없다는 그 모습에 왠지모를 반발심이 생기며 쉬이 발걸음을 떼기 싫었다."

    재영 "이름 어떻게 되세요?"

    show 채나연 땀
    with dissolve

    Unknown "뭐?"

    재영 "이름이요. 명색이 부원인데 동아리장 이름정돈 알아야죠."

    "성공했다."

    "아마 내가 발걸음을 떼지 않았던 이유는 저 벙찐 표정을 보기 위함이었던 것 같다."

    "동아리장은 한 5초동안 멍하니 있다가 생각을 정리하기 위함인지 시선을 잠시 아래로 내리고선 다시 나를 똑바로 보며 답해 주었다."

    나연 "채나연"

    재영 "나연누나시구나. 이름 예쁘네요. 그럼 전 신청서 내러 가보겠습니다!"

    나연 "......."

    "또 성공한 것 같다."

    hide 채나연

    "말을 뱉어버리고선 뒤를 돌아 바로 나가버려서 동아리장의 표정을 살펴진 못했지만 아무 반응이 없는 것으로 보아선 2차로 벙찐 것 같다."

    재영 "에이 몰라. 나중에 동아리 안가지 뭐."

    "나는 걸음을 재촉하여 교무실에 있는 선생님께 신청서를 내고 난 뒤에 교실로 돌아와서 아침의 사건들을 머릿 속에서 지웠다."

label 첫날_하교전 :

    scene 교실
    with fade

    play music "audio/대화할때 기본곡.mp3"

    "오늘은 어쩐지 정신없던 사건들이 많았지만 내일의 평화로운 일상을 위해서라 생각하고 평소와 같은 수업을 들으며 오후를 보내고 난 뒤 오후 수업을 모두 끝 마치게 되었다."

    show 정은하 신남

    은하 "재영~! 집가자!"

    "종이 울리고 종에 맞춰 아이들은 부산스레 자신의 짐을 챙기고 있었다."

    "이따금 복도에서 고함을 지르는 아이의 소리가 들려왔고, 옹기종기 모여 자기와 친한 아이들끼리 모여 수다를 떠는 모습도 보였다."

    은하 "재영, 뭐해?"

    "멍때리고 있던 와중. 내 시야에 은하의 모습이 가득 채워졌다."

    "항상 보던 얼굴이었는데 어쩐지 그리운 느낌에 불쑥 내밀어진 얼굴을 뚫어지게 쳐다보았다."

    "은하는 평소처럼 내가 질색하며 고개를 뒤로 뺄 줄 알았는지 예상외의 반응에 눈에 띄게 당황하면서 얼굴을 붉혔다."

    "…...하기야 내 친구가 나를 빤히 보면 나같아도 당황스럽긴 하겠다."

    "방금 내 행동엔 나도 이해가 가지 않았다."

    "그나저나 은하는 왜 얼굴이 붉지?"

    "어지간히 놀랐나보다. 아니면 화가 난건가?"

    은하 "ㅈ..집 언제 가게? 같이 가자. 오늘 힘들어 하던데."

    재영 "아 미안. 지금 가야지. 오늘 좀 멍하긴 한가봐."

    은하 "진짜 어디 안좋은 건 아니지? 안좋으면 나한테 말해야된다?"

    "은하는 뾰루퉁한 표정으로 나를 걱정해주었다."

    "오늘따라 생각이 많은 탓에 걱정을 끼친것이 미안하면서도 한편으론 고마웠다."

    재영 "몸이 안좋을리가, 점심에 실컷 먹었는 걸. 집이나 가자."

    은하 "그래~"

    hide 정은하

    "은하의 당황했던 표정은 나의 대답을 듣고는 금새 해맑은 웃음 뒤로 가려졌다."

    "말간 표정으로 대화를 이어나가며 실없는 농담을 주고받다보니 어느새 집에 도착하게되었다."

label 첫날_하교_집 :

    scene 남주집_night
    with fade

    재영 "오늘 뭔가 하루종일 멍하네."

    "꿨던 꿈 때문이었는지 유난히 소란스러웠던 오늘을 겪었기 때문인지."

    "머릿속에 실타래를 굴려놓은 듯 생각의 걸음이 여러번 끊어졌다."

    "무언가를 꽉 잡으면 될 것 같은데 미끄러운 손잡이 때문에 쉬이 잡아채지 못하는 상황이었다."

    "이런 생각을 하여도 더 이상의 진전은 없을 것 같아. 간단하게 몸을 씻고 침대에 누웠다."

    scene 재영방_night
    with fade

    "내일까지인 숙제가 없는지 머릿 속으로 체크하고 몸을 뉘인 상태에서 스마트폰을 만지작 거렸다."

    "눈이 분명 화면을 향하고 있었지만, 생각만은 아까 생각의 연장선이었다."

    "의미없음을 알아도 계속 생각하게 되는 상황이 가끔 있지않은가."

    "그렇게 몇 분이 지났을까."

label 둘째날_남주방:
    scene 재영방_day
    with fade

    "눈을 감고 다시 떠보니 창 사이로 햇빛이 비추었고 화면이 꺼진 핸드폰을 확인해보니 아침 8시였다."

    show 정은하 스탠딩
    with dissolve

    은하 "재영~! 일어나!!"

    "익숙한 목소리가 들렸다."

    "규칙적으로 늦잠을 자는 나를 깨우러오는 은하의 목소리."

    은하 "일어나자마자 폰 보네! 깨우러 온 나는 안보이냐!!"

    "어김없이 쨍한 목소리의 은하가 퉁명스러운 표정으로 날 바라보고 있었다."

    "이내 한 마디 더하려는 듯 은하가 가까이 다가오면서 말을 꺼냈다."

    은하 "재영아….너 어디아파? 땀을 왜 이렇게 흘려…?"

    "전혀 의식하지  못했다."

    "은하가 말해주고서야 내 얼굴이 식을 땀으로 적셔진 것을 느낄 수 있었다."

    재영 "아냐 그냥...악몽꿔서 그래. 금방 씻고 갈게."

    은하 "....괜찮은거 맞지? 아프면 이야기 해줘야 돼?"

    "영 못 미덥다는 얼굴로 나를 걱정스레 쳐다보던 은하는 나가겠다는 말을 하고도 몇 번이나 나의 상태를 살피고서 나갔다."

    "일단 웃는 얼굴로 은하의 등을 떠밀었다."

    hide 정은하

    "괜한 걱정을 끼치기 싫었기에."

    "실제로도 별 거 아닌 일이었다."

    "그저 기분나쁜 꿈을 꾸었을 뿐이다."

    "정말…. {w}기분 나쁜 꿈을 꾸었다."

    "그 꿈에 내가 아는 사람이 나왔던 거 같은데 누구였지…?"

    hide 정은하

label 캐릭터_루트_선택:
    window hide

    $renpy.call_screen("character_select_Screen")  

    if(character_select == 1):
        jump 은하_루트
    
    elif(character_select==2):
        jump 나연_루트

    elif(character_select==3):
        jump 지아_루트

label 은하_루트:
label 은하_둘째날_교실:

    "미구현 상태입니다."

    jump 미구현입니다

label 지아_루트:

    "미구현 상태입니다."

    jump 캐릭터_루트_선택

#나연루트를 탔을 때 2일차 교문부터 시작함
label 나연_루트:
label 둘째날_통학로:

    scene 통학로2
    with fade

    show 정은하 스탠딩
    with dissolve

    은하 "이번엔 지각 안하겠다. 여유롭네!"

    재영 "그러게, 오늘은 아침을 간단하게 먹어서 그런가."

    은하 "오랜만에 재영이가 해준 토스트 먹으니까 좋더라~?"

    "부산스러운 아침의 시작이었지만."

    "어제와 같이 촉박한 아침은 아니었다." 

    "빠른 샤워와 지각을 면하기 위한 토스트로 간단히 배를 채우니"

    "지각 걱정없이 등굣길을 걸을 수 있었다."

    "봄의 시작을 알리듯이 길가엔 소박한 색을 띈 들꽃들이 피었고"

    "겨울이 흘리고 간 조그마한 한기는 바람을 타고 맑은 공기를 뱉었다."

    재영 "아 맞다 은하야. 우리 숙제같은 건 없었지?"
 
    "간질거리는 봄내음을 온몸으로 느끼던 은하는 눈을 감은 채로 나에게 답해주었다."

    은하 "응~! 없었어. 넌 어째 어제일도 기억을 못하냐."

    재영 "내가 원래 좀 자주 깜빡해."

    은하 "으이그, 어릴 때도 사소한거 자주 까먹더니."

    재영 "그러게…."

    hide 정은하

    "등굣길에서의 대화는 너무나 일상적이고 평이해서"

    "있으면 모르고 없으면 아는 {w}그런 일상이었다."

label 둘째날_교문:
    scene 교문
    with fade

    show 정은하 스탠딩
    with dissolve

    은하 "오! 오늘은 일찍 도착했네! 학생회장도 없어!"

    "책가방이 신난 은하의 마음을 대변하듯 등에서 폴짝 뛰어올랐다."

    "교문을 향해 뛰어가는 발은 벌써 하교를 맞이하는 텐션이었다."

    "은하와 마찬가지로 나의 발걸음도 따라서 가벼워지고 있었다."

    "그와 반대로 머리는 매우 무거워지고 있었지만."

    재영 "은하야 나 오늘 동아리활동 하려고."

    은하 "엥. 갑자기?"

    재영 "동아리, 생각보다 괜찮더라고."

    "툭 걸리듯"

    "은하의 발걸음이 멈췄고."

    "고개를 돌려 멀뚱히 나를 3초정도 바라보았다."

    "아무 말 없이."

    "그리고선 장난스레 웃으며 말문을 텄다."

    은하 "우리 재영이 뭐, 맘에 드는 여자라도 있어~?"

    "나도 장난스레 마주 웃어주며 받아쳐줬다."

    재영 "그래. 엄청 예에쁜 여자 있으시다."

    은하 "어이구 좋으시겠어."

    hide 정은하

label 둘째날_교실:
    scene 교실
    with fade

    "어느새 계단을 다 올라서 교실이 있는 층에 오르게 된 우리는"

    "소란스러운 복도를 지나치고 문 앞에 다다르게 되었다."

    "은하는 문을 열며 흘러가는 투로 나에게 물었다."

    show 정은하 스탠딩
    with dissolve

    은하 "그래도 저녁은 해주는 거지?"

    "뒷모습에 가려 안보이는 낯이 웃는 표정이란 것을 강조한 듯 밝은 목소리였다."

    재영 "당연히 해주지. 그리 오래는 안할거야."

    은하 "그럼 다행이고!"

    "은하는 나의 대답에 휙 돌아보며 안도의 말을 뱉었다."

    "뒤를 돌아서 보여준 얼굴엔 웃음기가 배어나와 밝은 목소리와 어우러져 활짝 핀 꽃을 연상시켰다."

    "그리 대단치않은 요리실력을 좋아해주니 나로써는 고마울 따름이었다."

    "그렇게 지겨운 수업시간을 보내며 어느새 방과후가 되었다."

    "은하는 “먼저 갈게!”라고 하며 친구와 같이 집으로 돌아가고"

    "나도 주섬주섬 가방을 챙기고 아래층으로 발걸음을 옮겼다."

    hide 정은하

label 둘째날_채나연_동아리실에서의_마주침:
    scene 동아리실
    with fade

    play music "audio/동아리실음악.mp3"

    "역사문화탐구 동아리는 유령동아리인지라 별다른 활동이 없어서 동아리실에 매우 구석에 있었다."

    "예전에 아이들이 역사문화탐구 동아리에 대해 하는 이야기를 들은 적이 있었다."

    "아무도 활동을 하지않는 동아리인데 어떻게든 매년 동아리 부원을 채워서 동아리실을 차지하고 있으니 학교 선생님들이 좋은 시선으로 바라보지 않는다는 소문이었다."

    "그렇게 구석에 있는 동아리실을 꾸준히 혼자 독차지하는 선배에 대한 이야기도 나돌았다."

    재영 "어 선배 오셨네요?"

    show 채나연 스탠딩
    with dissolve

    나연 "....너 뭐야."

    "열린 동아리실 문쪽에 서있는 나연선배의 모습이 보였다."

    "걸어가면서 단어를 외우던 중이었는지 선배의 손엔 단어장이 들려있었다."

    재영 "선배가 동아리실 마음대로 써도 된다고해서 착실하게 쓰는 중이죠."

    나연 "......."

    재영 "이 동아리실 구석에 있어서 공부하기 좋은데 이런 장소를 안쓰긴 아깝잖아요."

    show 채나연 화남
    with dissolve

    나연 "하….."

    "골치 아픈 듯"

    "나연 선배는 관자놀이를 꾹꾹 누르며 눈을 지긋이 감았다."

    hide 채나연

    "전에 동아리실을 마음대로 써도 된다는 말을 한 적이 있기도 하고"

    "동아리 부원이기도 하여서 딱히 뭐라 할 말이 없었는지 나를 흘끗 보더니 별다른 말 없이 어제와 같은 자리에 앉아서 노트를 펼쳤다."

    "갑자기 변해버린 환경에 집중이 안될만도 한데 나연 선배는 내 존재가 더이상은 느껴지지 않는다는 듯 바로 공부에 집중하였다."

    "그런 선배를 슬며시 바라보다"

    "이내 나도 내일까지의 숙제와 공부를 시작하였다."

    "얼마나 시간이 지난 걸까"

    "창문으로 들어온 빛이 만들어준 그림자가 점점 기울어지고"

    "그림자 주위의 빛이 주황색으로 물들어갔다."

    "숙제는 끝낸지 오래였고"

    "오늘 배웠던 내용들을 정리하니 어느새 노을이 보였다.."

    "몇 시간동안 앉아있기만해서인지 몸이 굳어 찌뿌둥한 몸을 풀기위해 기지개를 피며  슬쩍 선배를 보았다."

    "몇 시간 전의 자세와 복장이 그대로여서"

    "선배의 시간만 멈춘 것 같았다."

    "언뜻보면 공부를 열심히 하는 여느 고등학생이었지만"

    "무언가 이질감이 드는 공기가 선배의 주위를 맴돌고 있었다."

    재영 "선배 여기요."

    show 채나연 스탠딩
    with dissolve

    나연 "........"

    "순간적으로 책상에서 나는 소리에"

    "선배는 곁눈질로 자신의 옆에 놓인 물건을 바라보았다."

    재영 "목도 마르실 것 같고, 커피 필요하실 거 같아서 사왔어요."

    나연 "너 내일부터 여기오지 마."

    재영 "넵 안올게요."

    "바로 긍정의 답을 받을 줄 몰랐는지."

    show 채나연 땀
    with dissolve

    "얼음장같던 표정사이로 당황이 흘러나왔다."

    "동아리실에 들어오고부터 나를 한 번도 바라본 적 없던 선배는"

    "이젠 나를 똑바로 응시하며 이상한 물체를 바라보듯 보고있었다."

    재영 "동아리장이 싫다는데 제가 억지로 들어올 순 없죠. 그래도 커피는 받아주시는 거죠?"

    show 채나연 화남
    with dissolve

    나연 "미친놈인가…."

    "웅얼거리는 입술사이로 작게 욕이 튀어나왔다."

    "그래도 생각해서 사준 건데….."

    "받을테니 얼른 꺼지라는 표시인건지 왼쪽에 내가 놓은 커피캔을 콱 쥐고 빠르게 자신의 오른쪽에 놔두었다."

    "그나마 커피캔이라도 받아준 것에 뿌듯함을 느끼며 더 이상 방해되지않도록 조심스레 짐을 챙긴 뒤 동아실을 나섰다."

    재영 "그럼 선배 저 먼저 가보겠습니다!"

    "당연히 예의바른 인사도 까먹지 않고 동아리실을 나갔다."

    stop music
    #검은화면
    scene 검은화면
    with fade
    

    "동아리실에서 공부를 안한지 벌써 2주일이 가까이 되었다."

    "덕분에 방과후에 은하와 함께 집으로 향할 수 있었지만."

    "이정도 기간이 지나니 선배의 얼굴이 살짝 가물가물할 정도다."

    scene 동아리실
    with fade

    play music "audio/동아리실음악.mp3"

    show 채나연 스탠딩
    with dissolve


    나연 "커피는 왜 자꾸 주는 거야."

    재영 "전에 커피는 받아주신다고 하셨잖아요."

    나연 "내가 언제."

    재영 "동아리 활동 첫날에요."

    나연 "동아리실에 오지 말랬잖아."

    재영 "그래서 커피만 두고 가잖아요."

    나연 "아니...하…."

    "물론 동아리실에서 공부만 안할 뿐이지"

    "선배에게 첫 날부터 매일 커피를 주고있었다."

    "커피를 전해주러 갈 때 자리에 없을 때가 많았지만"

    "항상 앉으시는 자리에 커피를 놔두면 다음 날엔 사라져있었다."

    "경계심이 강한 길고양이 밥 주는 느낌이어서 살짝 귀엽다는 느낌도 받았다."

    "길고양이가 생각난 김에 고양이 귀가 달린 선배를 상상할때 쯤 잔잔한 목소리의 선배가 나를 보며 물었다."

    나연 "솔직하게 말해. 너 무슨 생각이야."

    "신청서를 내러갔던 그때의 목소리같이 무심했지만"

    "그때와 다른 점이 있다면 어딘가 모르게 경계심이 어린 말투였다."

    재영 "무슨 생각은요. 전 그냥 커피드리고 싶었던건데."

    나연 "아무 목적이 없다기엔 너무 노골적이잖아."

    나연 "애초에 이 동아리 들어온 것부터 이상해."

    재영 "진짜 아무 목적없어요."

    재영 "이 동아리 들어온건 그냥 조용한 동아리활동 하고싶어서 그랬죠."

    나연 "아무 목적없이 커피 매일 챙겨주는게 정상적이야?"

    재영 "그렇다고 비정상적이진 않은 거 같은데요."

    나연 "말장난 하지말고 무슨 목적인건지 말해 1학년."

    재영 "벌써 제 이름 까먹으신건 아니죠?"

    나연 "학교 학생들 모두가 네 이름 못 까먹게 해줄까?"

    "점점 안좋아지는 표정의 나연선배가 보였다."

    "찡그리는 미간을 따라 꽉 쥐어지는 주먹에서 진심으로 화났다는 걸 느낄 수 있었다."

    "날 죽일 듯이 노려보는 표정이 순간적으로 날 누군가에 겹쳐본다는 느낌을 받았다."

    menu:
        "억울함의 눈물을 흘린다":
            jump 억울함의눈물

        "목적이 있었다고 한다":
            jump 목적이있었음

label 억울함의눈물:
    "사실대로 말했지만 믿어주지 않는 선배가 너무나 미웠다. 나는 그 설움을 이기지 못하고 결국은 눈물을 흘리고야 말았다."

    재영 "흑...흐윽...너무해요 선배."

    "아무리 차가운 선배라도 남자가 갑자기 우는 것이 당황스러웠는지"

    "선배가 조심히 다가오더니 살며시 내 멱살을 움켜쥐었다."

    "멱살? 어라?"

    show 채나연 땀
    with dissolve

    나연 "뒤질래? 입으로만 흑흑 거리면 누가 속냐?"

    jump 채나연_허락

label 목적이있었음:

    "질긴 눈싸움에 이길 자신이 없던 나는 슬며시 눈을 피하며 화두를 던졌다."

    jump 채나연_허락

label 채나연_허락:

    show 채나연 스탠딩
    with dissolve

    "더이상 목적이 없다고 무조건적인 부정을 했다간 오해가 확신이 되어버릴까 싶어서 일단 인정하기로 하였다."

    "그럴 줄 알았다는 표정으로 선배는 아무 말 없이 날 응시하고 있었다."

    "어서 빨리 진실을 털어놓으라는 그 표정에서 비친 눈빛이 사냥감을 노리는 맹수와도 같았다."

    "나는 천천히 이야기를 꺼냈다."

    재영 "이 동아리에 들어온 건 정말 우연이었어요. 앞서 설명한대로 적당한 동아리를 찾은 것 뿐이에요."

    나연 "하필 이 동아리를?"

    재영 "네. 되게 재미없어 보이더라고요. 그만큼 동아리활동도 별로 없을 것 같았고요. 실제로도 없잖아요."

    나연 "......."

    재영 "그리고 동아리 신청서를 동아리장에게 확인 받으러 동아리실에 갔고 선배 얼굴 볼 때까지도 별다른 계획이 없었어요."

    나연 "그럼?"

    재영 "선배 이름을 들은 순간 계획이 생겼죠."

    show 채나연 화남
    with dissolve

    "순간 선배의 얼굴이 험악해졌다."

    "무언가 짚이는 것이 있는 건지 아님단지 여러 가설들을 세우면서 최악의 가정을 골라 생각한건지."

    "점차 선배 주위의 공기가 험악해져가는 와중에 나는 평정을 유지하며 말을 이어갔다."

    재영 "아 이건 기회다 싶었어요."

    나연 "무슨 기회?"

    재영 "성적을 올릴 기회!"

    나연 "성적…..성적?"

    show 채나연 부끄
    with dissolve

    "처음 이름을 물어봤을 때 처럼 일순간 선배의 표정이 멍청해졌다."

    "진짜 난 이 표정을 보기위해서 이 동아리에 들어온게 아니었을까?"

    "성적이란 대답을 듣고나서 멍때리고 있는 선배."

    "동아리실 전체를 얼릴 것 같던 공기가 어느샌가 무너져있었다."

    "선배 이름 유명하잖아요. 전교2등을 모르면 간첩이죠."

    나연 "그래서 그거랑 네 성적이랑 무슨 관련인데."

    재영 "선배한테 공부 배우려고요."

    나연 "나한테?"

    재영 "예."

    나연 "누가 가르쳐준데?"

    show 채나연 땀
    with dissolve

    재영 "아님 말고요."

    "전부터 계속 빠른 수긍을 보여주는 나의 모습에 선배는 적잖이 당황한 모습을 보여주었다."

    show 채나연 스탠딩
    with dissolve

    "나와의 대화로 기가 빨린것인지. \n선배는 피곤한 표정으로 다시 눈을 공부하던 노트로 옮겼다."

    "언뜻보면 오해가 풀려서 자신의 일에 집중하는 것처럼 보였지만\n내 눈에는 아직도 전혀 의심을 놓지  않는 것 같았다."

    "다만 이상한 놈이라는 판단을 내리고 지금의 대화를 이어나가기 보단 공부를 하는 것이 더 효율적이라는 생각인 것 같다."

    재영 "선배. 아직 제가 의심스러우시면 확인하는 확실한 방법이 있잖아요."

    나연 "또 뭐."

    재영 "제가 선배 안보이는 곳에 있으면 무슨 짓을 할 줄 알고요. 가까이서 감시해야 되지않겠어요?"

    나연 "동아리실에서 공부하고 싶단거야?"

    재영 "네."

    나연 "하….맘대로 해. 이젠 신경 안쓸테니까."

    "역시 웃는 얼굴엔 침 못 뱉는다고"
    "정당한 이유로 예의바르게 부탁드리니 다시 동아리실에 들어오는 것을 허락해 주셨다."

    hide 채나연

    "한바탕 열띤 토론을 마치고나니 어느새 동아리실에는 노을빛이 짙게 깔리고 있었다."

    "노을을 호롱불 삼아 꿋꿋이 공부를 하는 선배의 샤프소리가 동아리실에 울렸다."

    "마침 허락도 받았겠다."

    "나는 슬며시 전에 앉았던 자리에 착석했다."

    "혹여나 선배가 불편해하지 않을까"

    "최대한 멀리, 대각선 끝 쪽 자리에 앉았다."

    "노을을 등지면서 앉은 뒤"

    "주머니에 있는 휴대폰을 꺼내어 은하에게 전화했다."

    #전화기 넣어야함
    #전화기 작업 후 후속 스크립트 작업 진행 예정
    show 정은하 휴대폰
    with dissolve

    재영 "은하야 너 먼저 가."

    은하 "엥?! 갑자기 왜?"

    재영 "나 동아리 활동하려고."

    재영 "요즘 별로 안했잖아."

    은하 "아…..알겠어. 그럼 먼저 간다!"

    재영 "그래."

    "은하의 목소리에는 항상 밝음이 묻어났다."

    "그만큼 은하의 성격이 밝다는 것의 방증 이기도 하였지만 상대방을 배려하고 있다는 마음도 많이 드러났다."

    hide 정은하

    "그때 대각선의 다른 끝쪽 자리에서 나연 선배의 목소리가 들려왔다."

    show 채나연 스탠딩
    with dissolve

    나연 "친구야?"

    "눈길도 주지 않으시면서 은근 할 말은 다 하신다."

    "방금 통화했던 은하와 나의 관계에 대해 궁금하신 듯 했다."

label 채나연_선택지1:

    menu:
        "그렇게 친하진 않아요":
            jump 채나연_선택지_그렇게친하진않아요

        "친구 맞아요":
            jump 채나연_선택지_친구맞아요

label 채나연_선택지_그렇게친하진않아요 :
    재영 "아뇨 뭐. 그렇게 친한사이는 아니에요."

    "방금 전까지 친하게 전화하던 사이를 그렇게 친한사이라고 한 것이 의심스러웠는지 잠시 날 응시하던 선배는 그러려니하면서 금방 긍정해주셨다."

    jump 채나연_선택지1_선택이후

label 채나연_선택지_친구맞아요 :
    재영 "친구 맞아요."

    재영 "저랑 소꿉친구에요."

    재영 "어릴때부터 엄청 친했었죠."

    jump 채나연_선택지1_선택이후

label 채나연_선택지1_선택이후 :
    나연 ".....그래."

    "단순히 친구가 맞는 지의 여부만 물어보려했는지 그 이상으로는 더 묻지 않으셨다."

    재영 "그럼 선배 저도 뭐 하나 여쭤봐도 되나요?"

    나연 "뭐."

    재영 "이 동아리에는 어떻게 들어오시게 된거에요?"

    나연 "여기 동아리 고문 선생님이 생기부 잘 적어주신다고해서."

    재영 "선배 희망하는 과가 문과계열인가요?"

    나연 "이과야. 그래서 이과 관련 동아리를 들어가려했는데. 대부분 노는 동아리이거나 생기부에 별로 적히는 게 없더라고."

    재영 "이과 중에서는 어느 과목 좋아하세요? 저는 그나마 생물이 재밌던데."

    나연 "나도 생물 좋아해."

    재영 "오 그럼 생물학과 가시는 거에요?"

    나연 "아니 의대가 목표야."
    
    재영 "아하 생물을 좋아하니까 의대도 좋겠네요."
    
    나연 "좋아서 가는 건 아니야."
    
    재영 "그럼요?"
    
    나연 "의대를 가기만 하면 가장 안정적으로 돈과 명예를 얻거든."
    
    재영 "에이 선배정도 머리면 연구실에서 일하셔도 되겠는데."
    
    나연 "과학고 애들도 의대가는 판국에 뭘."

    "상당히 적나라면서도 자극적인 내용의 말을 선배는 아무렇지 않게 하였다."

    "대답은 꼬박꼬박 해주면서도 손은 바삐 움직이는 선배를 향해 다시 질문을 던졌다."

    재영 "선배는 돈 많이 벌면 뭐할거에요?"

    나연 "몰라."

    재영 "근데 왜 돈을 벌고 싶으신 거예요?"

    나연 "몰라서 묻니. 돈 없으면 이용당하는 게 현대사회인데."

    재영 "힘들지 않아요?"

    "상당히 뜬금없는 질문이었을까."

    "기계처럼 움직이던 선배의 손이 질문을 듣고선 멈칫하였다."

    재영 "전 힘들거 같아서요. 혼자 공부하는 거. 뭐든 혼자 하는게 힘들잖아요."

    "나의 말의 방향이 궁금해서일까"

    "자신이 쓰던 글씨를 응시하던 눈이 어느새 나를 향해있었다."

    재영 "저 공부가르쳐 주시면 안될까요. 혼자는 너무 힘드네요."

    나연 "내가 왜."

    재영 "남한테 가르치면서 자기한테도 복습하는 효과가 된다네요. 개념 다진다는 생각으로 해주시면 안될까요."

    나연 "그러니까 내가 왜."

    재영 "같은 동아리 부원이잖아요."

    나연 "같은 동아리 부원한테 꼭 뭘 해줘야되는 건 아니야."

    재영 "안해주셔도 돼요. 그냥 같은 동아리 부원인 만큼 친하다는 걸 어필한거죠."

    나연 "안 친해."

    재영 "친해지면 안될까요?"

    나연 "꺼져."

    재영 "우와. 방금 저한테 욕 쓰신 거에요?"

    나연 "응."

    재영 "오늘 되게 밉보이기만 하는 거 같네요. 서럽다 서러워."

    "조금 더 남아있고싶었지만 7시가 다 되어가는 중이었기에.어쩔 수 없이 집에 갈 채비를 하였다."

    재영 "선배, 제가 저희 집 식충이 밥도 차려줘야하고 시간도 좀 늦어서요. 저 먼저 들어가보겠습니다."

    나연 "그러던가."

    재영 "내일 쪽지시험 있는데. 모르는 거 정리해서 내일 방과후 시간 때 말씀드릴게요!"

    나연 "아니 안가르쳐준다고."

    재영 "집에 조심히 들어가세요!"

    scene 재영방_night
    with fade

    "집에 돌아오니 7시가 다 되어갔다."
    "집안 거실에서는 우리집 식충이가 기다리고 있었다."

    "그새를 못참고 과자를 먹었는지 소파 근처에 과자 봉지가 널부러져 있었다."
    "재밌게 티비를 보다가 방금 들어온 나를 발견한 은하가 대충 손을 들어 반갑게 맞이해주었다."

    "가볍게 저녁을 차려주고선 같이 식사를 한 뒤 은하는 집으로 돌아갔고 나는 내 방에 올라갔다."

    "대충 침대에 누우면서"
    "내일 저녁 메뉴에 대해 생각했다."
    "그런 생각을 하다보니 문득 내가 은하 전속 요리사가 된 것 같았다."

    "은하와 같이 밥을 먹는 것이 이젠 일상이 되어서 가족처럼 느껴질 정도이다."
    "아니."
    "이정도면 가족이었다."
    "무조건적인 내 편이 되줄거라 생각되는 사람이 가족말고 무엇이 있을까."
    "평소에 내색하지는 않지만 가족의 빈자리를 채워주는 은하가 참 고마웠다."

    "간단한 샤워를 마친 후"
    "휴대폰을 들고선 온몸을 비비듯 침대에 누웠다."

    "멍했다."
    "내가 잘하고 있는 것인지 몰랐다."
    "스스로를 잃게 된다는 두려움이 있었지만."
    "내 선택들을 후회하진 않았다."

    "내가 알던 그 사람은"
    "힘듦을 목표로 이겨냈다."
    "목표 때문에 힘들어하지 않았고"
    "오히려 힘들었던 자신의 환경을 목표를 위해 견뎌내고 이겨냈다."

    "그러나 끝내 부러졌다."
    "잘 벼려진 칼 같던 그 사람은"
    "칼집이 없어서 결국 부서지고야 말았다."

    "칼집도 베어버릴 정도로 날카로웠기에"
    "그 누구도 칼집이 되어주려 하지않았고"
    "나조차도 쉬이 다가서지 못했다."

    "몇 번이고 실패한 뒤에서야 깨달았다."

    "아"
    "그건"
    "칼이 아니었구나."

    scene 동아리실
    with fade

    재영 "여기서 x의 해가 왜 2가 안되는 거에요?"

    show 채나연 스탠딩
    with dissolve

    나연 "조건을 봐. 문제 안에 답이 다 있다고."

    재영 "아 그러네. 오 선배 진짜 잘가르치는 거 같아요."

    나연 "나도 너같은 곳에서 막힌 적이 있었으니까. 다 경험이지."

    "평소때와 같은 동아리 활동이었다."
    "내가 모르는 문제를 몇 번 물어보고 헷갈리는 개념을 질문하니 의외로 답을 잘해주셨다."
    "귀찮을 텐데도 틱틱대며 꼬박꼬박 대답해주시는 선배가 조금 귀여웠다."

    "동아리방에 다시 공부할 수 있게된 후로"
    "선배에게 꾸준히 공부에 관련된 질문을 하였다."
    "그 결과 몇 개월 뒤의 시험에서 꽤나 좋은 성적을 받았고"
    "성적에 대해 선배에게 자랑하였다."

    "자랑할 당시엔 당연한 결과라는 듯이 태연한 대답을 해주셨지만"
    "내심 뿌듯함을 느끼셨던건지 그때부터 나의 질문에 좀 더 성실하게 답해주셨다."
    "물론 여전히 단답인건 여전하지만 말이다."

    나연 "설명 듣고있는거지?"

    "순간적으로 멍때리던 눈을 도르륵 굴려 선배쪽을 바라보니"
    "날 째려보는 선배가 보였다."

    재영 "선배 처음엔 저 가르치는 거 싫어하시더니 이젠 꽤 적극적이시네요?"

    나연 "나도 공부 되니까 그런거야."

    재영 "그래도 싫어하셨잖아요."

    show 채나연 화남
    with dissolve

    나연 "너 집중 안할거면 나가."

    "불만스럽게 펜을 돌리던 선배는 돌리던 펜을 멈추고 뾰족한 펜 끝으로 나를 가리켰다."
    "나름의 위협표시에도 나는 굴하지 않고 생글생글 웃어주기만 하였지만."
    "그런 표정이 맘에 안들었는지 인상을 찌푸리며 손에 있는 볼펜을 놓았다."

    show 채나연 스탠딩
    with dissolve

    나연 "잠시 쉬었다 하자."

    재영 "선배, 이번 주말에 저랑 같이 시내에 갈래요?"

    나연 "왜."
    
    재영 "참고서 사야해서요."

    나연 "근데 내가 왜."

    재영 "선생님이 같이 골라주셔야 좀 더 좋은 걸 사죠?"

    "선배는 잠시 생각하는 듯 하더니"
    "내 말에 일리가 있다고 판단했는지 조심스레 고개를 끄덕였다."

    재영 "최근에 시내 나가본 적이 드물었네요. {w} 선배는 가장 최근에 나가본게 언제에요? "

    나연 "나도 최근엔 안갔지. 나 혼자 가는 스타일도 아니니까 아마…."

    "기억을 되짚듯 위쪽을 바라보던 선배의 눈동자는"
    "잔잔한 물가에 돌멩이가 떨어진 것처럼 얕게떨렸다."

    "무언가를 떠올린 것일까"

    재영 "그래서 말인데 이번 주말에 같이 가주세요."

    "예의바르게 웃으면서 부탁드렸다."
    "그때 선배가 살며시 나에게 질문을 던졌다."
    "시선은 움직이지 않은채로"

    나연 "뜬금없는 질문인데."

    재영 "네. 말씀하세요."

    나연 "전에 너랑 통화했던 그 소꿉친구 있잖아."

    재영 "네."

    나연 "소꿉친구 정도면. 서로 의심같은 건 안하겠네?"

    재영 "하는데요?"

    나연 "응?"

    "나의 대답을 들으니 선배의 위로 올라가져있던 시선이 화들짝 놀라듯 순식간에 나를 향하고 있었다."

    재영 "얘가 숙제는 했나 밥은 먹었나 가끔 의심하죠."

    나연 "....그런 의심말고"

    재영 "아. 혹시 저 몰래 냉장고에 있는 아이스크림 먹었나 의심도 하죠."

    나연 "물어본 내가 잘못이지…."

    재영 "저희 그래서 주말에 언제 만날까요?"

    show 채나연 화남
    with dissolve

    나연 "하…."

label 채나연_데이트:

    scene 번화가
    with fade

    "미구현 상태입니다."

label 미구현입니다:

    scene 검은화면
    with fade

    "미구현 상태입니다."
