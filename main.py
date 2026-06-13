
import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠",
        "desc": "전략적이고 독립적인 당신은 강력한 지능과 목표 의식을 가진 뮤츠와 닮았어요."
    },
    "INTP": {
        "pokemon": "후딘",
        "emoji": "🔮",
        "desc": "호기심이 많고 분석적인 당신은 초능력으로 모든 것을 탐구하는 후딘 스타일!"
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥",
        "desc": "카리스마 넘치는 리더형! 목표를 향해 돌진하는 리자몽과 찰떡궁합입니다."
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "😏",
        "desc": "재치 있고 창의적인 당신은 장난기 많은 팬텀과 잘 어울려요."
    },
    "INFJ": {
        "pokemon": "루기아",
        "emoji": "🌊",
        "desc": "깊은 통찰력과 따뜻한 마음을 가진 당신은 신비로운 루기아와 닮았어요."
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "✨",
        "desc": "상상력이 풍부하고 순수한 당신은 무한한 가능성의 이브이!"
    },
    "ENFJ": {
        "pokemon": "픽시",
        "emoji": "💖",
        "desc": "사람들을 행복하게 만드는 당신은 사랑스러운 픽시와 비슷해요."
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "desc": "에너지 넘치고 매력적인 당신은 모두의 친구 피카츄!"
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🛡️",
        "desc": "책임감 있고 신뢰할 수 있는 당신은 든든한 거북왕 타입입니다."
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "🤗",
        "desc": "배려심이 깊고 따뜻한 당신은 모두를 치유하는 해피너스!"
    },
    "ESTJ": {
        "pokemon": "보스로라",
        "emoji": "⚙️",
        "desc": "체계적이고 추진력이 강한 당신은 강철 같은 보스로라와 닮았어요."
    },
    "ESFJ": {
        "pokemon": "푸크린",
        "emoji": "🎵",
        "desc": "친절하고 사교적인 당신은 분위기 메이커 푸크린!"
    },
    "ISTP": {
        "pokemon": "루카리오",
        "emoji": "🥋",
        "desc": "냉철하고 실용적인 당신은 강인한 루카리오와 환상의 조합!"
    },
    "ISFP": {
        "pokemon": "나인테일",
        "emoji": "🌸",
        "desc": "감성적이고 예술적인 당신은 우아한 나인테일과 잘 어울려요."
    },
    "ESTP": {
        "pokemon": "망나뇽",
        "emoji": "🚀",
        "desc": "모험을 사랑하는 당신은 자유로운 망나뇽 스타일!"
    },
    "ESFP": {
        "pokemon": "꼬부기",
        "emoji": "😄",
        "desc": "밝고 즐거운 당신은 어디서나 사랑받는 꼬부기!"
    }
}

st.markdown("""
<style>
.main {
    background: linear-gradient(180deg,#fef9ff,#f0f9ff);
}

.result-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    text-align: center;
    margin-top: 20px;
}

.title {
    text-align:center;
    font-size: 42px;
    font-weight: bold;
    color: #ff4b4b;
}

.subtitle {
    text-align:center;
    color:#666;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">⚡ MBTI 포켓몬 추천기 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">당신의 MBTI에 꼭 맞는 포켓몬을 찾아보세요! 🎮</div>',
    unsafe_allow_html=True
)

mbti = st.text_input(
    "🔍 MBTI를 입력하세요",
    placeholder="예: INFP"
).upper()

if st.button("🎁 포켓몬 추천받기!", use_container_width=True):

    if mbti in pokemon_data:

        st.balloons()

        info = pokemon_data[mbti]

        st.markdown(
            f"""
            <div class="result-card">
                <h1>{info['emoji']} {info['pokemon']}</h1>
                <h3>당신과 가장 잘 어울리는 포켓몬!</h3>
                <p style="font-size:18px;">
                    {info['desc']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(f"🎉 {mbti} 유형에게 추천되는 포켓몬은 '{info['pokemon']}' 입니다!")

        st.markdown("### 🌟 당신의 매력 포인트")
        st.write(
            "자신만의 강점을 가지고 있으며, 주변 사람들에게 긍정적인 영향을 주는 특별한 성격을 가지고 있어요!"
        )

    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요. (예: ENFP, INTJ)")

pokemon_images = {
    "피카츄": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    "뮤츠": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
    "이브이": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
}

st.image(pokemon_images["피카츄"], width=250)
