import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI로 찾는 나의 단짝 포켓몬",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 커스텀 CSS (따뜻한 크림·노란색 톤, 큰 글씨, 초보자 친화적 디자인)
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .stApp {
        background-color: #FFFDF0;
        color: #4A3E3D;
        font-family: 'Pretendard', 'Nanum Gothic', sans-serif;
    }
    
    /* 메인 타이틀 */
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        color: #D97706;
        margin-bottom: 0.3rem;
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #78350F;
        margin-bottom: 2rem;
    }

    /* 단짝 포켓몬 결과 카드 */
    .pokemon-card {
        background-color: #FFFFFF;
        border: 3px solid #FCD34D;
        border-radius: 20px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(217, 119, 6, 0.12);
        margin-top: 15px;
    }

    /* 포켓몬 이름 */
    .pokemon-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #B45309;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .pokemon-en-name {
        font-size: 1.1rem;
        color: #9CA3AF;
        margin-bottom: 15px;
    }

    /* 포켓몬 이미지 스타일 */
    .pokemon-img {
        width: 220px;
        height: 220px;
        object-fit: contain;
        filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.15));
        transition: transform 0.3s ease;
    }

    /* 정보 뱃지 태그 */
    .badge {
        display: inline-block;
        background-color: #FEF3C7;
        color: #92400E;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1rem;
        margin: 4px;
        border: 1px solid #FDE68A;
    }

    /* 어울리는 이유 박스 */
    .reason-box {
        background-color: #FFFBEB;
        border-left: 5px solid #F59E0B;
        padding: 16px;
        border-radius: 12px;
        text-align: left;
        margin-top: 20px;
        font-size: 1.1rem;
        line-height: 1.7;
        color: #78350F;
    }

    /* 선택 드롭다운 label 스타일 */
    label[data-testid="stWidgetLabel"] {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #B45309 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI - 포켓몬 데이터베이스 (PokeAPI 공식 이미지 링크 사용)
POKEMON_DATA = {
    "ISTJ": {
        "name": "거북왕",
        "en_name": "Blastoise",
        "type": "물 💧",
        "feature": "묵묵하고 신뢰감이 넘치는 단단한 리더",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "reason": [
            "원칙을 중요하게 생각하고 맡은 일에 책임감이 강한 ISTJ처럼, 항상 묵묵하게 팀을 지켜주는 든든한 단짝입니다.",
            "차분하고 침착한 성격으로 어떤 상황에서도 흐트러지지 않는 안정적인 시너지를 발휘합니다."
        ]
    },
    "ISFJ": {
        "name": "해피너스",
        "en_name": "Blissey",
        "type": "노말 🥚",
        "feature": "따뜻한 마음으로 주변을 돌보는 힐러",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "reason": [
            "타인의 필요를 세심하게 잘 챙기는 ISFJ와 꼭 닮은 포켓몬으로, 보는 것만으로도 주변 사람들을 행복하게 해줍니다.",
            "항상 곁에서 당신을 배려하고 챙겨주며 서로에게 큰 안식처가 되어줄 것입니다."
        ]
    },
    "INFJ": {
        "name": "가디안",
        "en_name": "Gardevoir",
        "type": "초능력 🔮 / 페어리 🧚",
        "feature": "깊은 통찰력과 강한 신념을 가진 수호자",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "reason": [
            "상대방의 마음을 깊이 이해하고 자신의 트레이너를 위해 모든 것을 바치는 충성심이 INFJ와 똑 닮았습니다.",
            "말하지 않아도 눈빛만으로 서로의 마음을 가장 잘 이해하는 깊은 영혼의 단짝이 됩니다."
        ]
    },
    "INTJ": {
        "name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "초능력 🔮",
        "feature": "독립적이고 뛰어난 지능을 가진 전략가",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "reason": [
            "혼자만의 생각에 깊이 빠져들고 늘 최고의 완벽을 추구하는 INTJ의 냉철하고 명석한 머리와 어울립니다.",
            "군더더기 없는 완벽한 계획으로 문제를 해결하는 지적인 파트너십을 형성합니다."
        ]
    },
    "ISTP": {
        "name": "루카리오",
        "en_name": "Lucario",
        "type": "격투 🥊 / 강철 ⚙️",
        "feature": "냉철한 상황 판단과 뛰어난 실천가",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "reason": [
            "말보다 행동으로 실력을 증명하고, 어떤 긴급한 위기 속에서도 냉정하게 대처하는 능력이 비슷합니다.",
            "서로의 영역을 존중하며 깔끔하고 효율적으로 목표를 이뤄냅니다."
        ]
    },
    "ISFP": {
        "name": "메타몽",
        "en_name": "Ditto",
        "type": "노말 🫠",
        "feature": "유연하고 유유자적한 자유로운 유연함",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "reason": [
            "어디에든 잘 맞춰주고 변화무쌍한 매력을 지닌 메타몽은 평화와 자유를 사랑하는 ISFP와 환상의 짝꿍입니다.",
            "틀에 매이지 않는 편안한 분위기로 당신의 유연한 일상을 적극 응원해 줍니다."
        ]
    },
    "INFP": {
        "name": "이브이",
        "en_name": "Eevee",
        "type": "노말 🌟",
        "feature": "무한한 가능성을 품은 순수한 꿈나무",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "reason": [
            "어떤 환경과 생각에 따라 다양한 모습으로 성장할 수 있는 풍부한 잠재력이 INFP의 상상력과 닮았습니다.",
            "따뜻하고 감성적인 매력으로 서로의 꿈을 함께 키워갈 수 있습니다."
        ]
    },
    "INTP": {
        "name": "고라파덕",
        "en_name": "Psyduck",
        "type": "물 🌊",
        "feature": "엉뚱하지만 숨겨진
