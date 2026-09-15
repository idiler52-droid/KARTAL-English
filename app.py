import streamlit as st
import random
import tempfile
import os
import re
import threading
import json
import urllib.request
import urllib.error
from datetime import date
import hashlib
import asyncio
import platform

# ============================================================
# K.A.R.T.A.L. ENGLISH
# Local English Learning Assistant
# ============================================================

st.set_page_config(
    page_title="K.A.R.T.A.L. English",
    page_icon="🦅",
    layout="wide"
)

# ============================================================
# LESSONS
# ============================================================

LESSONS = [
    {
        "word": "hello",
        "meaning": "merhaba",
        "example": "Hello, how are you?",
        "level": "A1"
    },
    {
        "word": "goodbye",
        "meaning": "hoşça kal",
        "example": "Goodbye, see you tomorrow.",
        "level": "A1"
    },
    {
        "word": "friend",
        "meaning": "arkadaş",
        "example": "He is my best friend.",
        "level": "A1"
    },
    {
        "word": "family",
        "meaning": "aile",
        "example": "I love my family.",
        "level": "A1"
    },
    {
        "word": "house",
        "meaning": "ev",
        "example": "My house is small.",
        "level": "A1"
    },
    {
        "word": "water",
        "meaning": "su",
        "example": "I want some water.",
        "level": "A1"
    },
    {
        "word": "food",
        "meaning": "yemek",
        "example": "The food is delicious.",
        "level": "A1"
    },
    {
        "word": "work",
        "meaning": "iş / çalışmak",
        "example": "I go to work every day.",
        "level": "A1"
    },
    {
        "word": "school",
        "meaning": "okul",
        "example": "My children go to school.",
        "level": "A1"
    },
    {
        "word": "happy",
        "meaning": "mutlu",
        "example": "I am very happy today.",
        "level": "A1"
    },
    {
        "word": "tired",
        "meaning": "yorgun",
        "example": "I am tired today.",
        "level": "A1"
    },
    {
        "word": "beautiful",
        "meaning": "güzel",
        "example": "This city is beautiful.",
        "level": "A1"
    },
    {
        "word": "important",
        "meaning": "önemli",
        "example": "This is very important.",
        "level": "A2"
    },
    {
        "word": "understand",
        "meaning": "anlamak",
        "example": "I understand you.",
        "level": "A2"
    },
    {
        "word": "remember",
        "meaning": "hatırlamak",
        "example": "I remember your name.",
        "level": "A2"
    },
]

# ============================================================
# SPEAKING SENTENCES
# 70+ DIFFERENT SENTENCES
# ============================================================

SPEAKING_SENTENCES = [

    # --------------------------------------------------------
    # INTRODUCTION - A1
    # --------------------------------------------------------

    {
        "id": 1,
        "category": "Tanışma",
        "level": "A1",
        "english": "Hello, my name is John.",
        "turkish": "Merhaba, benim adım John."
    },
    {
        "id": 2,
        "category": "Tanışma",
        "level": "A1",
        "english": "Nice to meet you.",
        "turkish": "Seninle tanıştığıma memnun oldum."
    },
    {
        "id": 3,
        "category": "Tanışma",
        "level": "A1",
        "english": "How are you today?",
        "turkish": "Bugün nasılsın?"
    },
    {
        "id": 4,
        "category": "Tanışma",
        "level": "A1",
        "english": "I am very happy today.",
        "turkish": "Bugün çok mutluyum."
    },
    {
        "id": 5,
        "category": "Tanışma",
        "level": "A1",
        "english": "I live in Turkey.",
        "turkish": "Türkiye'de yaşıyorum."
    },
    {
        "id": 6,
        "category": "Tanışma",
        "level": "A1",
        "english": "I am learning English.",
        "turkish": "İngilizce öğreniyorum."
    },
    {
        "id": 7,
        "category": "Tanışma",
        "level": "A1",
        "english": "I like listening to music.",
        "turkish": "Müzik dinlemeyi seviyorum."
    },
    {
        "id": 8,
        "category": "Tanışma",
        "level": "A1",
        "english": "I like watching movies.",
        "turkish": "Film izlemeyi seviyorum."
    },
    {
        "id": 9,
        "category": "Tanışma",
        "level": "A1",
        "english": "What is your name?",
        "turkish": "Senin adın ne?"
    },
    {
        "id": 10,
        "category": "Tanışma",
        "level": "A1",
        "english": "Where are you from?",
        "turkish": "Nerelisin?"
    },

    # --------------------------------------------------------
    # DAILY LIFE - A1
    # --------------------------------------------------------

    {
        "id": 11,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I wake up early every morning.",
        "turkish": "Her sabah erken uyanırım."
    },
    {
        "id": 12,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I drink coffee in the morning.",
        "turkish": "Sabahları kahve içerim."
    },
    {
        "id": 13,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I have breakfast at home.",
        "turkish": "Evde kahvaltı yaparım."
    },
    {
        "id": 14,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I go to work every day.",
        "turkish": "Her gün işe giderim."
    },
    {
        "id": 15,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I come home in the evening.",
        "turkish": "Akşam eve gelirim."
    },
    {
        "id": 16,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I am tired after work.",
        "turkish": "İşten sonra yorgun olurum."
    },
    {
        "id": 17,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I take a shower every day.",
        "turkish": "Her gün duş alırım."
    },
    {
        "id": 18,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I usually watch television at night.",
        "turkish": "Genellikle gece televizyon izlerim."
    },
    {
        "id": 19,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "I go to bed at eleven.",
        "turkish": "Saat on birde yatağa giderim."
    },
    {
        "id": 20,
        "category": "Günlük Hayat",
        "level": "A1",
        "english": "Today is a beautiful day.",
        "turkish": "Bugün güzel bir gün."
    },

    # --------------------------------------------------------
    # FOOD / RESTAURANT
    # --------------------------------------------------------

    {
        "id": 21,
        "category": "Restoran",
        "level": "A1",
        "english": "I would like a coffee, please.",
        "turkish": "Bir kahve istiyorum, lütfen."
    },
    {
        "id": 22,
        "category": "Restoran",
        "level": "A1",
        "english": "Can I have some water?",
        "turkish": "Biraz su alabilir miyim?"
    },
    {
        "id": 23,
        "category": "Restoran",
        "level": "A1",
        "english": "I would like a sandwich.",
        "turkish": "Bir sandviç istiyorum."
    },
    {
        "id": 24,
        "category": "Restoran",
        "level": "A1",
        "english": "The food is very good.",
        "turkish": "Yemek çok güzel."
    },
    {
        "id": 25,
        "category": "Restoran",
        "level": "A1",
        "english": "Can I see the menu, please?",
        "turkish": "Menüyü görebilir miyim, lütfen?"
    },
    {
        "id": 26,
        "category": "Restoran",
        "level": "A1",
        "english": "How much is the coffee?",
        "turkish": "Kahve ne kadar?"
    },
    {
        "id": 27,
        "category": "Restoran",
        "level": "A2",
        "english": "Could I have the bill, please?",
        "turkish": "Hesabı alabilir miyim, lütfen?"
    },
    {
        "id": 28,
        "category": "Restoran",
        "level": "A2",
        "english": "This restaurant is very popular.",
        "turkish": "Bu restoran çok popüler."
    },

    # --------------------------------------------------------
    # SHOPPING
    # --------------------------------------------------------

    {
        "id": 29,
        "category": "Alışveriş",
        "level": "A1",
        "english": "How much is this shirt?",
        "turkish": "Bu gömlek ne kadar?"
    },
    {
        "id": 30,
        "category": "Alışveriş",
        "level": "A1",
        "english": "I like this jacket.",
        "turkish": "Bu ceketi beğendim."
    },
    {
        "id": 31,
        "category": "Alışveriş",
        "level": "A1",
        "english": "Do you have a larger size?",
        "turkish": "Daha büyük beden var mı?"
    },
    {
        "id": 32,
        "category": "Alışveriş",
        "level": "A1",
        "english": "Do you have a smaller size?",
        "turkish": "Daha küçük beden var mı?"
    },
    {
        "id": 33,
        "category": "Alışveriş",
        "level": "A1",
        "english": "Can I pay by card?",
        "turkish": "Kartla ödeyebilir miyim?"
    },
    {
        "id": 34,
        "category": "Alışveriş",
        "level": "A2",
        "english": "I am just looking, thank you.",
        "turkish": "Sadece bakıyorum, teşekkür ederim."
    },
    {
        "id": 35,
        "category": "Alışveriş",
        "level": "A2",
        "english": "Is there a discount on this?",
        "turkish": "Bunda indirim var mı?"
    },

    # --------------------------------------------------------
    # TRAVEL
    # --------------------------------------------------------

    {
        "id": 36,
        "category": "Seyahat",
        "level": "A1",
        "english": "Where is the bus station?",
        "turkish": "Otobüs terminali nerede?"
    },
    {
        "id": 37,
        "category": "Seyahat",
        "level": "A1",
        "english": "Where is the train station?",
        "turkish": "Tren istasyonu nerede?"
    },
    {
        "id": 38,
        "category": "Seyahat",
        "level": "A1",
        "english": "I need a taxi.",
        "turkish": "Bir taksiye ihtiyacım var."
    },
    {
        "id": 39,
        "category": "Seyahat",
        "level": "A1",
        "english": "How can I get to the hotel?",
        "turkish": "Otele nasıl gidebilirim?"
    },
    {
        "id": 40,
        "category": "Seyahat",
        "level": "A1",
        "english": "Where is the airport?",
        "turkish": "Havaalanı nerede?"
    },
    {
        "id": 41,
        "category": "Seyahat",
        "level": "A2",
        "english": "I have a reservation at the hotel.",
        "turkish": "Otelde rezervasyonum var."
    },
    {
        "id": 42,
        "category": "Seyahat",
        "level": "A2",
        "english": "What time does the train leave?",
        "turkish": "Tren saat kaçta kalkıyor?"
    },

    # --------------------------------------------------------
    # WORK
    # --------------------------------------------------------

    {
        "id": 43,
        "category": "İş",
        "level": "A1",
        "english": "I work from Monday to Friday.",
        "turkish": "Pazartesiden cumaya çalışırım."
    },
    {
        "id": 44,
        "category": "İş",
        "level": "A1",
        "english": "I am busy today.",
        "turkish": "Bugün meşgulüm."
    },
    {
        "id": 45,
        "category": "İş",
        "level": "A1",
        "english": "I have a meeting today.",
        "turkish": "Bugün bir toplantım var."
    },
    {
        "id": 46,
        "category": "İş",
        "level": "A1",
        "english": "I need some help.",
        "turkish": "Biraz yardıma ihtiyacım var."
    },
    {
        "id": 47,
        "category": "İş",
        "level": "A2",
        "english": "I have a lot of work today.",
        "turkish": "Bugün çok işim var."
    },
    {
        "id": 48,
        "category": "İş",
        "level": "A2",
        "english": "I will finish this work tomorrow.",
        "turkish": "Bu işi yarın bitireceğim."
    },

    # --------------------------------------------------------
    # DAILY CONVERSATION
    # --------------------------------------------------------

    {
        "id": 49,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "What are you doing?",
        "turkish": "Ne yapıyorsun?"
    },
    {
        "id": 50,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "I am watching a movie.",
        "turkish": "Film izliyorum."
    },
    {
        "id": 51,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "What time is it?",
        "turkish": "Saat kaç?"
    },
    {
        "id": 52,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "See you tomorrow.",
        "turkish": "Yarın görüşürüz."
    },
    {
        "id": 53,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "Have a nice day.",
        "turkish": "İyi günler."
    },
    {
        "id": 54,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "Thank you very much.",
        "turkish": "Çok teşekkür ederim."
    },
    {
        "id": 55,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "You are welcome.",
        "turkish": "Rica ederim."
    },
    {
        "id": 56,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "I don't understand.",
        "turkish": "Anlamıyorum."
    },
    {
        "id": 57,
        "category": "Günlük Konuşma",
        "level": "A1",
        "english": "Please speak slowly.",
        "turkish": "Lütfen yavaş konuş."
    },
    {
        "id": 58,
        "category": "Günlük Konuşma",
        "level": "A2",
        "english": "Could you repeat that, please?",
        "turkish": "Bunu tekrar edebilir misiniz, lütfen?"
    },

    # --------------------------------------------------------
    # FAMILY / HOME
    # --------------------------------------------------------

    {
        "id": 59,
        "category": "Aile ve Ev",
        "level": "A1",
        "english": "My family is very important to me.",
        "turkish": "Ailem benim için çok önemli."
    },
    {
        "id": 60,
        "category": "Aile ve Ev",
        "level": "A1",
        "english": "I live with my family.",
        "turkish": "Ailemle yaşıyorum."
    },
    {
        "id": 61,
        "category": "Aile ve Ev",
        "level": "A1",
        "english": "My house is near the city center.",
        "turkish": "Evim şehir merkezine yakın."
    },
    {
        "id": 62,
        "category": "Aile ve Ev",
        "level": "A1",
        "english": "My room is very small.",
        "turkish": "Odam çok küçük."
    },
    {
        "id": 63,
        "category": "Aile ve Ev",
        "level": "A2",
        "english": "I usually clean my room on Sunday.",
        "turkish": "Genellikle pazar günü odamı temizlerim."
    },

    # --------------------------------------------------------
    # HOBBIES
    # --------------------------------------------------------

    {
        "id": 64,
        "category": "Hobiler",
        "level": "A1",
        "english": "I like playing computer games.",
        "turkish": "Bilgisayar oyunları oynamayı seviyorum."
    },
    {
        "id": 65,
        "category": "Hobiler",
        "level": "A1",
        "english": "I enjoy listening to music.",
        "turkish": "Müzik dinlemekten hoşlanırım."
    },
    {
        "id": 66,
        "category": "Hobiler",
        "level": "A1",
        "english": "I like watching football.",
        "turkish": "Futbol izlemeyi seviyorum."
    },
    {
        "id": 67,
        "category": "Hobiler",
        "level": "A2",
        "english": "I often watch movies at the weekend.",
        "turkish": "Hafta sonları sık sık film izlerim."
    },
    {
        "id": 68,
        "category": "Hobiler",
        "level": "A2",
        "english": "I want to improve my English.",
        "turkish": "İngilizcemi geliştirmek istiyorum."
    },
    {
        "id": 69,
        "category": "Hobiler",
        "level": "A2",
        "english": "Learning English is very useful.",
        "turkish": "İngilizce öğrenmek çok faydalıdır."
    },
    {
        "id": 70,
        "category": "Hobiler",
        "level": "A2",
        "english": "I practice English every day.",
        "turkish": "Her gün İngilizce pratik yaparım."
    },
]

# ============================================================
# SESSION STATE
# ============================================================

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "speaking_queue" not in st.session_state:
    st.session_state.speaking_queue = []

if "speaking_history" not in st.session_state:
    st.session_state.speaking_history = []

if "last_speaking_id" not in st.session_state:
    st.session_state.last_speaking_id = None

if "current_sentence" not in st.session_state:
    st.session_state.current_sentence = None

if "quiz_queue" not in st.session_state:
    st.session_state.quiz_queue = []

if "quiz_current" not in st.session_state:
    st.session_state.quiz_current = None

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = False

if "conversation_question" not in st.session_state:
    st.session_state.conversation_question = None

if "conversation_last_answer" not in st.session_state:
    st.session_state.conversation_last_answer = ""

if "conversation_used_questions" not in st.session_state:
    st.session_state.conversation_used_questions = []

# Öğrenme istatistikleri
if "quiz_correct" not in st.session_state:
    st.session_state.quiz_correct = 0

if "speaking_attempts" not in st.session_state:
    st.session_state.speaking_attempts = 0

if "speaking_correct" not in st.session_state:
    st.session_state.speaking_correct = 0

# Öğrenme motoru: konu bazlı güçlü/zayıf alan takibi
if "topic_stats" not in st.session_state:
    st.session_state.topic_stats = {}

if "daily_goal" not in st.session_state:
    st.session_state.daily_goal = {
        "xp": 100,
        "questions": 10,
        "speaking": 5,
    }

if "daily_progress" not in st.session_state:
    st.session_state.daily_progress = {
        "xp": 0,
        "questions": 0,
        "speaking": 0,
    }

if "daily_date" not in st.session_state:
    st.session_state.daily_date = str(__import__("datetime").date.today())

if "conversation_attempts" not in st.session_state:
    st.session_state.conversation_attempts = 0

if "conversation_correct" not in st.session_state:
    st.session_state.conversation_correct = 0

if "last_speech_audio_hash" not in st.session_state:
    st.session_state.last_speech_audio_hash = None

if "last_conversation_audio_hash" not in st.session_state:
    st.session_state.last_conversation_audio_hash = None

if "last_xp_gain" not in st.session_state:
    st.session_state.last_xp_gain = None

if "level_up_message" not in st.session_state:
    st.session_state.level_up_message = None

if "tts_audio" not in st.session_state:
    st.session_state.tts_audio = None

if "tts_audio_text" not in st.session_state:
    st.session_state.tts_audio_text = ""

if "activity_date" not in st.session_state:
    st.session_state.activity_date = str(date.today())

if "streak" not in st.session_state:
    st.session_state.streak = 1

if "daily_xp" not in st.session_state:
    st.session_state.daily_xp = 0

# ============================================================
# XP / LEVEL SYSTEM
# ============================================================

def get_level_info(xp=None):
    """K.A.R.T.A.L. oyun seviyesi: her 100 XP = 1 seviye."""
    if xp is None:
        xp = st.session_state.xp
    level = max(1, (xp // 100) + 1)
    current_xp = xp % 100
    return level, current_xp, 100, current_xp / 100


def add_xp(amount, reason=""):
    """XP ekler; seviye atlama mesajını güvenli şekilde gösterir."""
    old_level, _, _, _ = get_level_info()
    gained = max(0, int(amount))
    st.session_state.xp += gained
    st.session_state.daily_xp += gained
    new_level, _, _, _ = get_level_info()
    st.session_state.level = new_level

    if gained > 0:
        st.session_state.last_xp_gain = {
            "amount": gained,
            "reason": reason,
        }

    if new_level > old_level:
        st.session_state.level_up_message = (
            f"🎉 Seviye atladınız! **K.A.R.T.A.L. Seviyesi {new_level}**"
        )


def smart_xp_from_score(score, correct=True):
    """Cevap kalitesine göre 0/5/10/15/20 XP belirler."""
    score = max(0, min(100, int(score or 0)))
    if not correct:
        return 0, "Cevap henüz doğru değil"
    if score >= 95:
        return 20, "🔥 Mükemmel cevap"
    if score >= 85:
        return 15, "⭐ Çok iyi cevap"
    if score >= 70:
        return 10, "🟢 Doğru cevap"
    if score >= 50:
        return 5, "🟠 Anlaşılır cevap"
    return 0, "Cevap geliştirilmeli"


def get_accuracy(correct, total):
    if total <= 0:
        return 0
    return round((correct / total) * 100)


def register_activity():
    """Oturum içindeki günlük çalışma serisini günceller."""
    today = str(date.today())
    if st.session_state.activity_date != today:
        st.session_state.activity_date = today
        st.session_state.streak += 1

# ============================================================
# SPEAKING QUEUE
# ============================================================

def build_speaking_queue(category="Tümü", level="Tümü"):

    filtered = []

    for sentence in SPEAKING_SENTENCES:

        category_ok = (
            category == "Tümü"
            or sentence["category"] == category
        )

        level_ok = (
            level == "Tümü"
            or sentence["level"] == level
        )

        if category_ok and level_ok:
            filtered.append(sentence)

    if not filtered:
        return []

    ids = [x["id"] for x in filtered]

    random.shuffle(ids)

    # Önceki cümlenin hemen tekrar gelmesini engelle
    if (
        len(ids) > 1
        and st.session_state.last_speaking_id is not None
        and ids[0] == st.session_state.last_speaking_id
    ):
        ids[0], ids[1] = ids[1], ids[0]

    return ids


def get_next_sentence(category="Tümü", level="Tümü"):

    # Queue boşsa yeni torba oluştur
    if not st.session_state.speaking_queue:

        st.session_state.speaking_queue = build_speaking_queue(
            category,
            level
        )

    if not st.session_state.speaking_queue:
        return None

    next_id = st.session_state.speaking_queue.pop(0)

    sentence = next(
        (
            x for x in SPEAKING_SENTENCES
            if x["id"] == next_id
        ),
        None
    )

    if sentence:
        st.session_state.last_speaking_id = sentence["id"]

    return sentence

# ============================================================
# TTS
# ============================================================

def _cloud_tts_audio(text):
    """Bulutta Edge TTS ile İngilizce sesi MP3 olarak üretir."""
    import edge_tts

    async def generate():
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural",
            rate="-5%",
        )
        chunks = []
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                chunks.append(chunk["data"])
        return b"".join(chunks)

    return asyncio.run(generate())


def speak_text(text):
    """Windows'ta pyttsx3, Streamlit Cloud/Linux'ta Edge TTS kullanır."""
    if not text:
        return

    # Yerel Windows kullanımında mevcut TTS davranışını koru.
    if platform.system().lower() == "windows":
        try:
            import pyttsx3

            def run_speech():
                try:
                    engine = pyttsx3.init()
                    voices = engine.getProperty("voices")
                    selected_voice = None
                    for voice in voices:
                        voice_text = (
                            str(getattr(voice, "name", "")) + " " +
                            str(getattr(voice, "id", ""))
                        ).lower()
                        if "english" in voice_text or "en-us" in voice_text or "en-gb" in voice_text:
                            selected_voice = voice.id
                            break
                    if selected_voice:
                        engine.setProperty("voice", selected_voice)
                    engine.setProperty("rate", 145)
                    engine.setProperty("volume", 1.0)
                    engine.say(text)
                    engine.runAndWait()
                    engine.stop()
                except Exception:
                    pass

            threading.Thread(target=run_speech, daemon=True).start()
            return
        except Exception:
            pass

    # Streamlit Cloud Linux: tarayıcıda oynatılacak MP3 üret.
    try:
        audio = _cloud_tts_audio(text)
        st.session_state.tts_audio = audio
        st.session_state.tts_audio_text = text
    except Exception as e:
        st.warning(
            "Bulut ses sistemi şu anda sesi üretemedi. "
            "Metni okuyarak devam edebilirsiniz."
        )

# ============================================================
# WHISPER
# ============================================================

@st.cache_resource
def load_whisper():

    try:

        from faster_whisper import WhisperModel

        model = WhisperModel(
            "tiny.en",
            device="cpu",
            compute_type="int8"
        )

        return model

    except Exception as e:

        st.error(
            f"Whisper modeli yüklenemedi: {e}"
        )

        return None


def transcribe_audio(audio_file):

    model = load_whisper()

    if model is None:
        return ""

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp:

            temp.write(
                audio_file.getvalue()
            )

            temp_path = temp.name

        segments, info = model.transcribe(
            temp_path,
            beam_size=1
        )

        text = " ".join(
            segment.text
            for segment in segments
        )

        return text.strip()

    except Exception as e:

        st.error(
            f"Ses analiz edilemedi: {e}"
        )

        return ""

    finally:

        if temp_path and os.path.exists(temp_path):

            try:
                os.remove(temp_path)
            except Exception:
                pass

# ============================================================
# SPEECH SCORE
# ============================================================

def normalize_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def speech_score(target, spoken):

    target_words = normalize_text(
        target
    ).split()

    spoken_words = normalize_text(
        spoken
    ).split()

    if not target_words:
        return 0

    if not spoken_words:
        return 0

    matched = 0

    for word in target_words:

        if word in spoken_words:
            matched += 1

    score = int(
        (matched / len(target_words)) * 100
    )

    # Ufak bir tolerans
    if score > 100:
        score = 100

    return score

# ============================================================
# QUIZ QUEUE
# ============================================================

def build_quiz():

    questions = list(LESSONS)

    random.shuffle(questions)

    return questions


def get_quiz_question():

    if not st.session_state.quiz_queue:
        st.session_state.quiz_queue = build_quiz()

    if not st.session_state.quiz_queue:
        return None

    return st.session_state.quiz_queue.pop(0)

# ============================================================
# OLLAMA / HERMES - REAL CONVERSATION
# ============================================================

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
OLLAMA_MODEL = "hermes3:3b"


def ask_ollama(messages, max_tokens=120):
    """Ollama üzerinden yerel Hermes modeliyle konuş."""
    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": max_tokens,
        },
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result.get("message", {}).get("content", "").strip()

    except urllib.error.URLError as e:
        raise RuntimeError(
            "Ollama'ya bağlanılamadı. Ollama'nın çalıştığından emin olun."
        ) from e
    except Exception as e:
        raise RuntimeError(f"Ollama hatası: {e}") from e


def extract_json(text):
    """Hermes JSON dışında metin döndürürse JSON kısmını ayıkla."""
    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    start = text.find("{")
    end = text.rfind("}")

    if start >= 0 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except Exception:
            pass

    return None


def _conversation_question_bank():
    """Seviyeye göre seçilen konuşma soru havuzu."""
    return [
        # ---------------- A1 ----------------
        {"level":"A1","english":"What is your name?","turkish":"Adın ne?"},
        {"level":"A1","english":"Where are you from?","turkish":"Nerelisin?"},
        {"level":"A1","english":"Where do you live?","turkish":"Nerede yaşıyorsun?"},
        {"level":"A1","english":"How old are you?","turkish":"Kaç yaşındasın?"},
        {"level":"A1","english":"What do you do?","turkish":"Ne iş yapıyorsun?"},
        {"level":"A1","english":"What is your favorite color?","turkish":"En sevdiğin renk nedir?"},
        {"level":"A1","english":"What is your favorite food?","turkish":"En sevdiğin yemek nedir?"},
        {"level":"A1","english":"Do you like music?","turkish":"Müzik sever misin?"},
        {"level":"A1","english":"Do you like watching movies?","turkish":"Film izlemeyi sever misin?"},
        {"level":"A1","english":"Do you like reading books?","turkish":"Kitap okumayı sever misin?"},
        {"level":"A1","english":"Do you have a pet?","turkish":"Evcil hayvanın var mı?"},
        {"level":"A1","english":"What time do you wake up?","turkish":"Saat kaçta uyanırsın?"},
        {"level":"A1","english":"What do you do in the morning?","turkish":"Sabahları ne yaparsın?"},
        {"level":"A1","english":"What do you usually eat for breakfast?","turkish":"Kahvaltıda genellikle ne yersin?"},
        {"level":"A1","english":"What is the weather like today?","turkish":"Bugün hava nasıl?"},
        {"level":"A1","english":"What sport do you like?","turkish":"Hangi sporu seversin?"},
        {"level":"A1","english":"Can you make coffee?","turkish":"Kahve yapabilir misin?"},
        {"level":"A1","english":"What do you do for fun?","turkish":"Eğlenmek için ne yaparsın?"},

        # ---------------- A2 ----------------
        {"level":"A2","english":"What did you do yesterday?","turkish":"Dün ne yaptın?"},
        {"level":"A2","english":"What did you eat today?","turkish":"Bugün ne yedin?"},
        {"level":"A2","english":"What are you going to do tomorrow?","turkish":"Yarın ne yapacaksın?"},
        {"level":"A2","english":"What are your plans for the weekend?","turkish":"Hafta sonu planların neler?"},
        {"level":"A2","english":"Have you ever traveled abroad?","turkish":"Hiç yurt dışına çıktın mı?"},
        {"level":"A2","english":"How do you usually travel?","turkish":"Genellikle nasıl seyahat edersin?"},
        {"level":"A2","english":"What city would you like to visit?","turkish":"Hangi şehri ziyaret etmek istersin?"},
        {"level":"A2","english":"Which country would you like to visit?","turkish":"Hangi ülkeyi ziyaret etmek istersin?"},
        {"level":"A2","english":"What kind of music do you like?","turkish":"Ne tür müzik seversin?"},
        {"level":"A2","english":"How often do you practice English?","turkish":"Ne sıklıkla İngilizce pratik yaparsın?"},
        {"level":"A2","english":"Why are you learning English?","turkish":"Neden İngilizce öğreniyorsun?"},
        {"level":"A2","english":"What do you usually do on weekends?","turkish":"Hafta sonları genellikle ne yaparsın?"},
        {"level":"A2","english":"What do you usually do after work?","turkish":"İşten sonra genellikle ne yaparsın?"},
        {"level":"A2","english":"What makes you happy?","turkish":"Seni ne mutlu eder?"},
        {"level":"A2","english":"What would you like to learn?","turkish":"Ne öğrenmek istersin?"},
        {"level":"A2","english":"What food can you cook?","turkish":"Hangi yemekleri yapabilirsin?"},
        {"level":"A2","english":"What is difficult about English?","turkish":"İngilizcede zor olan şey nedir?"},

        # ---------------- B1 ----------------
        {"level":"B1","english":"What is something you would like to change about your daily routine?","turkish":"Günlük rutininde değiştirmek istediğin bir şey nedir?"},
        {"level":"B1","english":"Tell me about a trip you really enjoyed.","turkish":"Çok keyif aldığın bir seyahati anlat."},
        {"level":"B1","english":"What is the best decision you have ever made?","turkish":"Hayatında verdiğin en iyi karar nedir?"},
        {"level":"B1","english":"What do you usually do when you have a difficult problem?","turkish":"Zor bir problemin olduğunda genellikle ne yaparsın?"},
        {"level":"B1","english":"What are the advantages of learning English?","turkish":"İngilizce öğrenmenin avantajları nelerdir?"},
        {"level":"B1","english":"Do you prefer working alone or with other people, and why?","turkish":"Tek başına mı yoksa başka insanlarla mı çalışmayı tercih edersin, neden?"},
        {"level":"B1","english":"What kind of person do you enjoy spending time with?","turkish":"Nasıl insanlarla vakit geçirmekten hoşlanırsın?"},
        {"level":"B1","english":"What is one skill you would like to improve this year?","turkish":"Bu yıl geliştirmek istediğin bir beceri nedir?"},
        {"level":"B1","english":"How has technology changed your daily life?","turkish":"Teknoloji günlük hayatını nasıl değiştirdi?"},
        {"level":"B1","english":"What makes a good friend?","turkish":"İyi bir arkadaşı iyi yapan şey nedir?"},
        {"level":"B1","english":"If you had a free week, where would you go?","turkish":"Bir hafta boş zamanın olsaydı nereye giderdin?"},
        {"level":"B1","english":"What is something you learned from a difficult experience?","turkish":"Zor bir deneyimden öğrendiğin bir şey nedir?"},

        # ---------------- B2 ----------------
        {"level":"B2","english":"How do you think social media affects the way people communicate?","turkish":"Sence sosyal medya insanların iletişim kurma biçimini nasıl etkiliyor?"},
        {"level":"B2","english":"What are the biggest challenges people face when trying to learn a foreign language?","turkish":"İnsanların yabancı dil öğrenirken karşılaştığı en büyük zorluklar nelerdir?"},
        {"level":"B2","english":"Do you think technology makes life better or more complicated? Explain your opinion.","turkish":"Sence teknoloji hayatı daha iyi mi yoksa daha karmaşık mı yapıyor? Görüşünü açıkla."},
        {"level":"B2","english":"If you could change one thing about your city, what would you change and why?","turkish":"Şehrinle ilgili bir şeyi değiştirebilseydin neyi değiştirirdin ve neden?"},
        {"level":"B2","english":"What qualities do you think a successful leader should have?","turkish":"Sence başarılı bir lider hangi özelliklere sahip olmalı?"},
        {"level":"B2","english":"Should people work fewer hours if technology can do more of their jobs? Why or why not?","turkish":"Teknoloji işlerin daha fazlasını yapabiliyorsa insanlar daha az saat çalışmalı mı? Neden?"},
        {"level":"B2","english":"What is an important problem in modern society that people should talk about more?","turkish":"Modern toplumda insanların daha fazla konuşması gereken önemli bir sorun nedir?"},
        {"level":"B2","english":"How would you describe the difference between a good job and a meaningful job?","turkish":"İyi bir iş ile anlamlı bir iş arasındaki farkı nasıl açıklarsın?"},
    ]


def _target_cefr_level():
    """Oyun seviyesini CEFR konuşma seviyesine çevirir."""
    game_level = st.session_state.get("level", 1)
    if game_level <= 3:
        return "A1"
    if game_level <= 6:
        return "A2"
    if game_level <= 9:
        return "B1"
    return "B2"


def normalize_conversation_question(question):
    bank = _conversation_question_bank()
    if isinstance(question, dict):
        english = str(question.get("english", "")).strip()
        valid = next((q for q in bank if q["english"] == english), None)
        if valid:
            return valid.copy()
    return generate_conversation_question()


def generate_conversation_question():
    """Oyuncunun seviyesine uygun, daha önce sorulmamış soru seç."""
    bank = _conversation_question_bank()
    target = _target_cefr_level()
    used = st.session_state.conversation_used_questions

    available = [
        q for q in bank
        if q["level"] == target and q["english"] not in used
    ]

    # O seviyenin havuzu biterse aynı seviyeyi baştan başlat.
    if not available:
        used[:] = [
            q for q in used
            if not any(x["english"] == q and x["level"] == target for x in bank)
        ]
        available = [q for q in bank if q["level"] == target]

    if not available:
        available = [q for q in bank if q["level"] == target]

    question = random.choice(available)
    if question["english"] not in used:
        used.append(question["english"])
    return question.copy()

def evaluate_conversation_answer(question, answer):
    """
    K.A.R.T.A.L. English Conversation Engine v2

    Hedef:
    - Kullanıcının birebir "kitap cevabı" vermesini zorunlu tutmamak.
    - Doğal kısa cevapları kabul etmek.
    - Aynı anlamı taşıyan farklı cümleleri kabul etmek.
    - "Anlam doğru / grammar hatalı" durumunu ayırmak.
    - Whisper'ın küçük hatalarına tolerans göstermek.
    - Sorunun istediği bilgi türünü dikkate almak.
    - Emin olunmayan durumlarda Hermes 3B'yi ikinci değerlendirme katmanı olarak kullanmak.
    """
    import re

    current_question = (
        question.get("english", "")
        if isinstance(question, dict)
        else str(question)
    ).strip()

    student = " ".join(str(answer).strip().split())

    def result(
        correct,
        reply="",
        correction="",
        correct_answer="",
        confidence="high",
        score=100,
    ):
        return {
            "correct": bool(correct),
            "reply": reply or (
                "Doğru! Çok iyi."
                if correct
                else "Cevabın bu soruyu henüz karşılamıyor."
            ),
            "correction": correction,
            "correct_answer": correct_answer,
            "confidence": confidence,
            "score": max(0, min(100, int(score))),
            "next_question": (
                generate_conversation_question()
                if correct
                else None
            ),
        }

    def words(text):
        return re.findall(r"[a-zA-Z]+(?:['’][a-zA-Z]+)?", text.lower())

    def normalized(text):
        value = str(text or "").strip()
        value = re.sub(r"\s+", " ", value)
        return value

    def norm_words(text):
        return set(words(text))

    def has_any(text, values):
        return bool(norm_words(text) & set(values))

    def has_phrase(text, patterns):
        low = text.lower()
        return any(re.search(pattern, low) for pattern in patterns)

    def strip_whisper_repeats(text):
        parts = text.split()
        out = []
        for part in parts:
            clean = part.lower().strip(".,!?;:")
            if out and clean == out[-1].lower().strip(".,!?;:"):
                continue
            out.append(part)
        return " ".join(out)

    answer_clean = strip_whisper_repeats(normalized(student))
    a_low = answer_clean.lower().strip(" ?.!")
    a_words = norm_words(answer_clean)
    q_low = current_question.lower().strip(" ?.!")
    q_words = norm_words(current_question)

    if not answer_clean:
        return result(
            False,
            "Cevap alınamadı.",
            "Mikrofon konuşmanızı anlayamadı. Lütfen aynı soruya kısa bir İngilizce cevap verin.",
            confidence="high",
            score=0,
        )

    # --------------------------------------------------------
    # COMMON LEXICAL GROUPS
    # --------------------------------------------------------
    yes_words = {"yes", "yeah", "yep", "sure", "absolutely", "of course"}
    no_words = {"no", "nope", "nah", "not"}

    # --------------------------------------------------------
    # UNIVERSAL SHORT YES / NO ANSWERS
    # --------------------------------------------------------
    # "Yes." ve "No." yes/no sorularına doğal ve tamamlanmış
    # cevaplardır. Soruyu tekrar etmeleri gerekmez.
    yes_no_question = bool(re.match(
        r"^(do|does|did|am|is|are|was|were|can|could|will|would|"
        r"have|has|had|should|shall|may|might|must)\\b",
        q_low,
    ))

    if yes_no_question:
        short_answer = a_low.strip(".,!?")
        if short_answer in {"yes", "yeah", "yep", "sure", "absolutely"}:
            return result(
                True,
                "Evet! Bu doğru ve doğal bir kısa cevap.",
                confidence="high",
                score=100,
            )

        if short_answer in {"no", "nope", "nah"}:
            return result(
                True,
                "Doğru! Bu doğal ve geçerli bir kısa cevap.",
                confidence="high",
                score=100,
            )

    positive_words = {
        "like", "love", "enjoy", "prefer", "favorite", "favourite",
        "want", "would", "enjoys"
    }
    place_words = {
        "in", "at", "from", "near", "home", "house", "city", "town",
        "village", "country", "turkey", "türkiye", "istanbul", "ankara",
        "izmir", "bursa", "kutahya", "kütahya", "beach", "park", "school",
        "office", "hotel", "restaurant", "airport", "station", "center",
        "centre", "abroad", "here", "there"
    }
    transport_words = {
        "bus", "car", "train", "plane", "airplane", "taxi", "metro",
        "tram", "bike", "bicycle", "walk", "walking", "drive", "driving",
        "fly", "flying"
    }
    frequency_words = {
        "always", "usually", "often", "sometimes", "rarely", "never",
        "every", "once", "twice", "daily", "weekly", "monthly",
        "week", "weeks", "month", "months", "day", "days", "morning",
        "weekend", "weekends"
    }
    time_words = {
        "morning", "afternoon", "evening", "night", "noon", "midnight",
        "oclock", "am", "pm"
    }
    weather_words = {
        "sunny", "rainy", "cloudy", "windy", "snowy", "cold", "hot",
        "warm", "cool", "beautiful", "nice", "bad", "clear", "stormy"
    }
    activity_words = {
        "watch", "watching", "read", "reading", "play", "playing", "work",
        "working", "study", "studying", "learn", "learning", "listen",
        "listening", "eat", "eating", "drink", "drinking", "sleep",
        "sleeping", "cook", "cooking", "clean", "cleaning", "go", "going",
        "come", "coming", "visit", "visiting", "travel", "traveling",
        "practice", "practicing", "exercise", "exercising", "walk",
        "walking", "meet", "meeting", "relax", "relaxing"
    }

    # --------------------------------------------------------
    # 1) HAVE YOU EVER ...?
    # --------------------------------------------------------
    if re.match(r"^have you(?: ever)?\b", q_low):
        yes = bool(re.match(r"^(yes|yeah|yep|sure|absolutely|of course)\b", a_low))
        no = bool(re.match(r"^(no|nope|nah)\b", a_low))

        has_have = bool(re.search(r"\bhave\b", a_low))
        has_havent = bool(re.search(r"\b(?:haven['’]?t|have not)\b", a_low))
        has_experience = has_any(
            a_low,
            {
                "traveled", "travelled", "visited", "been", "gone",
                "seen", "tried", "eaten", "met", "worked", "studied"
            },
        )

        if (yes or no) and (has_have or has_havent):
            return result(True, "Doğru! Çok iyi.")

        if yes and has_experience:
            return result(True, "Doğru! Cevabın doğal ve anlaşılır.")

        if no and has_havent:
            return result(True, "Doğru! Çok iyi.")

        if (yes or no) and has_any(a_low, {"am", "is", "are"}):
            return result(
                False,
                "Cevabın anlaşılır, ancak yardımcı fiil yanlış.",
                "Bu soru 'Have you ever...?' ile başlıyor. Kısa cevapta 'have / haven't' kullanmalısın.",
                "Yes, I have." if yes else "No, I haven't.",
            )

        if has_experience or has_any(
            a_low,
            {"abroad", "before", "once", "twice", "never"}
        ):
            return result(True, "Doğru! Cevabın soruyu karşılıyor.", confidence="medium")

    # --------------------------------------------------------
    # 2) DO YOU HAVE ...?
    # --------------------------------------------------------
    have_match = re.match(r"^do you (have .+)$", q_low)
    if have_match:
        subject = have_match.group(1)
        subject_words = norm_words(subject)
        yes = bool(re.match(r"^(yes|yeah|yep|sure|of course)\b", a_low))
        no = bool(re.match(r"^(no|nope|nah)\b", a_low))

        has_have = bool(re.search(r"\bhave\b", a_low))
        has_not_have = bool(
            re.search(r"\b(?:don['’]?t|do not|no)\b", a_low)
        )

        # "No pets.", "No brothers or sisters."
        content = a_words - {
            "yes", "yeah", "yep", "sure", "of", "course",
            "no", "nope", "nah", "not", "i", "do", "dont", "don't",
            "have", "has", "any", "a", "an", "the", "my", "some",
            "very", "one", "ones"
        }

        # Kısa ama bağlama uygun cevap.
        if no and (content or has_not_have):
            return result(True, "Doğru! Cevabın soruyu karşılıyor.")

        if yes and (has_have or content):
            return result(True, "Doğru! Cevabın soruyu karşılıyor.")

        if has_not_have and content:
            return result(True, "Doğru! Cevabın doğal ve anlaşılır.")

        if has_have and content:
            return result(True, "Doğru! Cevabın doğal ve anlaşılır.")

        # "Yes." / "No." tek başına da anlamlıdır; fakat daha açık cevap öner.
        if yes or no:
            return result(
                True,
                "Doğru! Kısa cevap verdin.",
                "Daha doğal ve öğretici olması için tam cevap da verebilirsin.",
                "Yes, I do." if yes else "No, I don't.",
                confidence="medium",
                score=90,
            )

    # --------------------------------------------------------
    # 3) DO YOU ...? — LIKE / GENERAL ACTION
    # --------------------------------------------------------
    do_match = re.match(r"^do you (.+)$", q_low)
    if do_match:
        subject = do_match.group(1).strip()
        subject_words = norm_words(subject)

        yes = bool(re.match(r"^(yes|yeah|yep|sure|of course)\b", a_low))
        no = bool(re.match(r"^(no|nope|nah|not really)\b", a_low))
        has_do = bool(re.search(r"\bdo\b", a_low))
        has_dont = bool(re.search(r"\b(?:don['’]?t|do not)\b", a_low))
        has_am = bool(re.search(r"\b(?:am|is|are)\b", a_low))

        if (yes or no) and has_am and not (has_do or has_dont):
            return result(
                False,
                "Cevabın anlaşılır, ancak yardımcı fiil yanlış.",
                "Bu soru 'Do you...?' ile başlıyor. Kısa cevapta 'do / don't' kullanılır.",
                "Yes, I do." if yes else "No, I don't.",
            )

        if yes and has_do:
            return result(True, "Doğru! Çok iyi.")

        if no and has_dont:
            return result(True, "Doğru! Çok iyi.")

        if subject.startswith("like "):
            target = subject[5:].strip()
            target_words = norm_words(target)

            if (
                has_any(a_low, {"like", "love", "enjoy", "prefer"})
                and target_words & a_words
            ):
                return result(True, "Doğru! Cevabın doğal ve anlaşılır.")

            # "Rock music." gibi bağlamsal kısa cevap.
            if target_words & a_words and len(a_words) >= 1:
                return result(
                    True,
                    "Doğru! Bağlamdan neyi sevdiğin anlaşılıyor.",
                    "Tam cümle kurmak istersen: 'I like ...'",
                    confidence="medium",
                    score=90,
                )

        # "Do you play any sports?" -> "Football." gibi cevaplar.
        if subject.startswith(("play ", "do ", "watch ", "read ", "eat ", "drink ")):
            if len(a_words) >= 1 and not (yes or no):
                return result(
                    True,
                    "Doğru! Cevabın soruyu karşılıyor.",
                    "İstersen tam cümleyle de söyleyebilirsin.",
                    confidence="medium",
                    score=90,
                )

    # --------------------------------------------------------
    # 4) ARE / CAN / DID / WILL — YES/NO
    # --------------------------------------------------------
    aux_patterns = [
        (
            r"^are you\b",
            "are",
            "am",
            "aren't",
            "Yes, I am.",
            "No, I'm not.",
        ),
        (
            r"^can you\b",
            "can",
            "can",
            "can't",
            "Yes, I can.",
            "No, I can't.",
        ),
        (
            r"^did you\b",
            "did",
            "did",
            "didn't",
            "Yes, I did.",
            "No, I didn't.",
        ),
        (
            r"^will you\b",
            "will",
            "will",
            "won't",
            "Yes, I will.",
            "No, I won't.",
        ),
    ]

    for pattern, q_aux, a_aux, negative_aux, yes_form, no_form in aux_patterns:
        if re.match(pattern, q_low):
            yes = bool(re.match(r"^(yes|yeah|yep|sure|of course)\b", a_low))
            no = bool(re.match(r"^(no|nope|nah|not really)\b", a_low))

            if yes and re.search(rf"\b{re.escape(a_aux)}\b", a_low):
                return result(True, "Doğru! Çok iyi.")

            if no and re.search(rf"\b{re.escape(negative_aux)}\b", a_low):
                return result(True, "Doğru! Çok iyi.")

            # Doğal uzun cevaplar: "I can swim", "I am tired", "I went..."
            if q_aux == "can" and has_any(a_low, {"can", "able", "yes"}):
                return result(True, "Doğru! Cevabın soruyu karşılıyor.", confidence="medium")

            if q_aux == "are" and has_any(
                a_low,
                {"am", "i'm", "tired", "happy", "fine", "busy", "ready", "okay"}
            ):
                return result(True, "Doğru! Cevabın soruyu karşılıyor.", confidence="medium")

            if q_aux == "did" and (
                has_any(
                    a_low,
                    {
                        "did", "went", "ate", "watched", "played", "visited",
                        "worked", "stayed", "saw", "bought", "made", "had"
                    },
                )
                or "yesterday" in a_words
                or "last" in a_words
            ):
                return result(True, "Doğru! Geçmiş zamandaki cevabın anlaşılır.", confidence="medium")

            if q_aux == "will" and has_any(
                a_low,
                {"will", "going", "tomorrow", "plan", "plans"}
            ):
                return result(True, "Doğru! Cevabın gelecekle ilgili.", confidence="medium")

            if (yes or no) and has_any(
                a_low,
                {"am", "is", "are", "do", "does", "did", "can", "will"}
            ):
                return result(
                    False,
                    "Cevabın anlaşılır, ancak yardımcı fiil yanlış.",
                    f"Bu soru '{q_aux}' ile başlıyor. Kısa cevapta uygun yardımcı fiili kullanmalısın.",
                    yes_form if yes else no_form,
                )

    # --------------------------------------------------------
    # 5) NAME
    # --------------------------------------------------------
    if q_low == "what is your name":
        if (
            has_phrase(a_low, [r"\bmy name is\b", r"\bi['’]?m\b"])
            and len(a_words) >= 2
        ) or len(a_words) >= 1:
            return result(
                True,
                "Doğru! Tanıştığımıza memnun oldum.",
                "" if has_phrase(a_low, [r"\bmy name is\b"]) else
                "İstersen daha doğal olarak: 'My name is ...' diyebilirsin.",
                confidence="high",
                score=100,
            )

    # --------------------------------------------------------
    # 6) WHERE ...?
    # --------------------------------------------------------
    if q_low.startswith("where "):
        has_location = bool(place_words & a_words)
        has_place_phrase = has_phrase(
            a_low,
            [
                r"\blive\b",
                r"\bstay\b",
                r"\bwork\b",
                r"\bstudy\b",
                r"\bgo\b",
                r"\bcome\b",
                r"\bvisit\b",
                r"\bfrom\b",
                r"\bnear\b",
                r"\bin\b",
                r"\bat\b",
            ],
        )

        # Özel isim veya tek kelimelik yer cevabı.
        capitalized = [
            p.strip(".,!?")
            for p in answer_clean.split()
            if len(p.strip(".,!?")) > 2 and p[:1].isupper()
        ]

        if has_location or has_place_phrase or capitalized:
            return result(True, "Doğru! Çok iyi.")

        return result(
            False,
            "Cevabın bir yer bilgisi vermiyor.",
            "Bu soru bir yer soruyor. Örneğin: 'I live in Kütahya.' veya 'In Turkey.'",
            "I live in Kütahya.",
        )

    # --------------------------------------------------------
    # 7) HOW OLD ...?
    # --------------------------------------------------------
    if q_low.startswith("how old "):
        if (
            re.search(r"\b\d{1,3}\b", a_low)
            or re.search(r"\b(?:years? old)\b", a_low)
        ):
            return result(True, "Doğru! Çok iyi.")

        number_words = {
            "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"
        }
        if a_words & number_words:
            return result(True, "Doğru! Yaşını belirttin.")

        return result(
            False,
            "Cevabın yaş belirtmiyor.",
            "Bu soru yaşını soruyor. Örneğin: 'I am 30 years old.'",
            "I am 30 years old.",
        )

    # --------------------------------------------------------
    # 8) WHAT TIME ...?
    # --------------------------------------------------------
    if q_low.startswith("what time "):
        has_numeric_time = bool(
            re.search(r"\b\d{1,2}(?::\d{2})?\b", a_low)
        )
        has_time_context = bool(time_words & a_words)

        number_time_words = {
            "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve"
        }

        if has_numeric_time or has_time_context or (
            a_words & number_time_words
        ):
            return result(True, "Doğru! Saat bilgisini verdin.")

        return result(
            False,
            "Cevabın saat belirtmiyor.",
            "Bu soru saat soruyor. Örneğin: 'At seven.' veya 'I wake up at seven.'",
            "I wake up at seven.",
        )

    # --------------------------------------------------------
    # 9) HOW OFTEN ...?
    # --------------------------------------------------------
    if q_low.startswith("how often "):
        if frequency_words & a_words:
            return result(True, "Doğru! Sıklığı doğru belirttin.")

        if re.search(r"\b\d+\s*(?:time|times)\b", a_low):
            return result(True, "Doğru! Sıklığı belirttin.")

        return result(
            False,
            "Cevabın sıklık belirtmiyor.",
            "Bu soru 'Ne sıklıkla?' diye soruyor. Örneğin: 'Every day.' veya 'Twice a week.'",
            "I practice English every day.",
        )

    # --------------------------------------------------------
    # 10) WHY ...?
    # --------------------------------------------------------
    if q_low.startswith("why "):
        if has_any(a_low, {"because", "since"}) and len(a_words) >= 2:
            return result(True, "Doğru! Nedenini açıkladın.")

        # "To improve my English." gibi infinitive cevaplar.
        if re.match(r"^to\b", a_low) and len(a_words) >= 3:
            return result(True, "Doğru! Nedenini kısa ve doğal şekilde açıkladın.")

        if len(a_words) >= 4 and has_any(
            a_low,
            {"want", "need", "like", "love", "important", "help", "learn"}
        ):
            return result(
                True,
                "Doğru! Cevabından nedenin anlaşılıyor.",
                "Daha açık bir neden için 'Because ...' ile başlayabilirsin.",
                confidence="medium",
                score=90,
            )

        return result(
            False,
            "Cevabın sorunun nedenini açıklamıyor.",
            "Bu soru 'Neden?' diye soruyor. 'Because...' ile başlayan kısa bir neden verebilirsin.",
            "Because I want to improve my English.",
        )

    # --------------------------------------------------------
    # 11) WHAT MAKES / WHAT IS IMPORTANT / WHAT ARE YOU GOOD AT
    # --------------------------------------------------------
    if "what makes you" in q_low:
        if len(a_words) >= 2 and not (
            a_low in {"yes", "no", "i am", "i'm fine", "okay"}
        ):
            return result(True, "Doğru! Cevabın anlamlı bir şey belirtiyor.")
        return result(
            False,
            "Cevabın sorunun istediği şeyi belirtmiyor.",
            "Seni neyin mutlu ettiğini veya güldürdüğünü söylemelisin. Örneğin: 'Music makes me happy.'",
            "Music makes me happy.",
        )

    if "what are you good at" in q_low:
        if len(a_words) >= 1 and (
            activity_words & a_words
            or has_any(a_low, {"good", "great", "can", "at"})
        ):
            return result(True, "Doğru! Bir beceri belirttin.", confidence="medium")
        return result(
            False,
            "Cevabın bir beceri belirtmiyor.",
            "Örneğin: 'I am good at cooking.' veya 'I am good at football.'",
            "I am good at cooking.",
        )

    if "what is important to you" in q_low:
        if len(a_words) >= 2:
            return result(True, "Doğru! Senin için önemli olan şeyi belirttin.")
        return result(
            False,
            "Cevabın yeterince bilgi vermiyor.",
            "Örneğin: 'My family is important to me.'",
            "My family is important to me.",
        )

    # --------------------------------------------------------
    # 12) WEATHER
    # --------------------------------------------------------
    if "what is the weather like" in q_low:
        if weather_words & a_words or len(a_words) >= 2:
            return result(True, "Doğru! Hava durumunu anlattın.", confidence="medium")
        return result(
            False,
            "Cevabın hava durumunu belirtmiyor.",
            "Örneğin: 'It is sunny today.' veya 'It is cold.'",
            "It is sunny today.",
        )

    # --------------------------------------------------------
    # 13) FAVORITE ...
    # --------------------------------------------------------
    favorite_match = re.match(r"^what is your favorite (.+)$", q_low)
    if favorite_match:
        thing = favorite_match.group(1).strip()

        if has_any(a_low, positive_words) and len(a_words) >= 2:
            return result(True, "Doğru! Cevabın doğal ve anlaşılır.")

        if re.search(r"\bmy favorite\b", a_low) and len(a_words) >= 3:
            return result(True, "Doğru! Çok iyi.")

        # "Pizza.", "Blue.", "Tarkan." gibi bağlamsal cevaplar.
        if len(a_words) >= 1 and not (
            a_words <= yes_words or a_words <= no_words
        ):
            return result(
                True,
                "Doğru! Cevabın sorunun istediği bilgiyi veriyor.",
                "İstersen tam cümleyle: 'My favorite ... is ...' diyebilirsin.",
                confidence="medium",
                score=90,
            )

        return result(
            False,
            "Cevabın favorini belirtmiyor.",
            f"Bu soru en sevdiğin {thing} bilgisini istiyor. Örneğin: 'My favorite {thing} is ...'",
            f"My favorite {thing} is ...",
        )

    # --------------------------------------------------------
    # 14) WHAT CITY / COUNTRY / PLACE WOULD YOU LIKE TO VISIT?
    # --------------------------------------------------------
    if "what city would you like to visit" in q_low:
        if (
            has_any(a_low, {"visit", "would", "like", "want"})
            and len(a_words) >= 2
        ) or (len(a_words) >= 1 and not (a_words & yes_words | a_words & no_words)):
            return result(True, "Doğru! Ziyaret etmek istediğin yeri belirttin.")
        return result(
            False,
            "Bir şehir belirtmen gerekiyor.",
            "Örneğin: 'I would like to visit Istanbul.'",
            "I would like to visit Istanbul.",
        )

    if "which country would you like to visit" in q_low:
        if (
            len(a_words) >= 1
            and not (a_words & yes_words | a_words & no_words)
        ):
            return result(True, "Doğru! Ziyaret etmek istediğin ülkeyi belirttin.")
        return result(
            False,
            "Bir ülke belirtmen gerekiyor.",
            "Örneğin: 'I would like to visit Italy.'",
            "I would like to visit Italy.",
        )

    # --------------------------------------------------------
    # 15) HOW DO YOU USUALLY TRAVEL?
    # --------------------------------------------------------
    if "how do you usually travel" in q_low:
        if transport_words & a_words:
            return result(True, "Doğru! Nasıl seyahat ettiğini belirttin.")
        return result(
            False,
            "Cevabın ulaşım şeklini belirtmiyor.",
            "Örneğin: 'I usually travel by bus.'",
            "I usually travel by bus.",
        )

    # --------------------------------------------------------
    # 16) WHO ...?
    # --------------------------------------------------------
    if q_low.startswith("who "):
        if len(a_words) >= 1 and not (
            a_words <= yes_words or a_words <= no_words
        ):
            return result(True, "Doğru! Bir kişi belirttin.", confidence="medium")

        return result(
            False,
            "Bu soru bir kişi soruyor.",
            "Bir kişinin adını veya kim olduğunu belirtmelisin. Örneğin: 'Tarkan is my favorite singer.'",
            "My favorite singer is Tarkan.",
        )

    # --------------------------------------------------------
    # 17) WHAT DID ...? / PAST
    # --------------------------------------------------------
    if q_low.startswith("what did "):
        past_words = {
            "went", "ate", "watched", "played", "visited", "worked",
            "stayed", "saw", "bought", "made", "had", "was", "were",
            "did", "studied", "cleaned", "cooked", "called", "came",
            "got", "went"
        }

        if (
            past_words & a_words
            or "yesterday" in a_words
            or "last" in a_words
            or len(a_words) >= 3
        ):
            return result(
                True,
                "Doğru! Geçmişte yaptığın şeyi anlattın.",
                "Geçmiş zaman cümlesini mümkün olduğunca net söylemeye çalış.",
                confidence="medium" if not (past_words & a_words) else "high",
                score=90 if not (past_words & a_words) else 100,
            )

        return result(
            False,
            "Cevabın geçmişte ne yaptığını belirtmiyor.",
            "Örneğin: 'I watched a movie yesterday.'",
            "I watched a movie yesterday.",
        )

    # --------------------------------------------------------
    # 18) WHAT ARE YOU DOING / TODAY?
    # --------------------------------------------------------
    if "what are you doing" in q_low:
        if re.search(r"\b[a-z]+ing\b", a_low) or activity_words & a_words:
            return result(True, "Doğru! Şu anda ne yaptığını anlattın.")
        return result(
            False,
            "Cevabın şu anda ne yaptığını belirtmiyor.",
            "Örneğin: 'I am watching TV.'",
            "I am watching TV.",
        )

    if "what are you doing today" in q_low:
        if activity_words & a_words or len(a_words) >= 3:
            return result(True, "Doğru! Bugünkü planını anlattın.", confidence="medium")
        return result(
            False,
            "Bugün ne yaptığını veya yapacağını belirtmelisin.",
            "Örneğin: 'I am working today.'",
            "I am working today.",
        )

    # --------------------------------------------------------
    # 19) PLANS / TOMORROW
    # --------------------------------------------------------
    if "plans for the weekend" in q_low or "going to do tomorrow" in q_low:
        if has_any(
            a_low,
            {"will", "going", "plan", "plans", "tomorrow", "weekend"}
        ) or activity_words & a_words:
            return result(True, "Doğru! Planını anlattın.", confidence="medium")
        return result(
            False,
            "Cevabın gelecek planını belirtmiyor.",
            "Örneğin: 'I am going to visit my family.'",
            "I am going to visit my family.",
        )

    # --------------------------------------------------------
    # 20) WHAT DO YOU DO / WHAT DO YOU ...?
    # --------------------------------------------------------
    if q_low.startswith("what do you do"):
        if has_any(
            a_low,
            {
                "work", "job", "teacher", "engineer", "driver", "doctor",
                "student", "business", "manager", "shop", "office"
            }
        ) or len(a_words) >= 2:
            return result(True, "Doğru! Ne yaptığını anlattın.", confidence="medium")
        return result(
            False,
            "Ne yaptığını belirtmen gerekiyor.",
            "Örneğin: 'I work in an office.' veya 'I am a teacher.'",
            "I work in an office.",
        )

    if q_low.startswith("what do you "):
        if activity_words & a_words or len(a_words) >= 2:
            return result(True, "Doğru! Cevabın soruyu karşılıyor.", confidence="medium")
        return result(
            False,
            "Cevabın sorunun istediği bilgiyi vermiyor.",
            "Sorunun istediği eylem veya bilgiyi kısa bir İngilizce cümleyle söyle.",
        )

    # --------------------------------------------------------
    # 21) WHAT KIND OF MUSIC / SPORT / FOOD / ETC.
    # --------------------------------------------------------
    if "what kind of" in q_low or "what sport" in q_low:
        if len(a_words) >= 1 and not (a_words & yes_words | a_words & no_words):
            return result(
                True,
                "Doğru! Tercihini belirttin.",
                "İstersen tam cümleyle: 'I like ...'",
                confidence="medium",
                score=90,
            )
        return result(
            False,
            "Bir tür veya tercih belirtmen gerekiyor.",
            "Örneğin: 'I like rock music.'",
            "I like rock music.",
        )

    # --------------------------------------------------------
    # 22) WHAT WOULD YOU LIKE TO LEARN?
    # --------------------------------------------------------
    if "what would you like to learn" in q_low:
        if has_any(a_low, {"learn", "want", "would", "like"}) and len(a_words) >= 2:
            return result(True, "Doğru! Öğrenmek istediğin şeyi belirttin.")

        if len(a_words) >= 1 and not (a_words & yes_words | a_words & no_words):
            return result(
                True,
                "Doğru! Ne öğrenmek istediğin anlaşılıyor.",
                "Daha doğal bir cümle: 'I would like to learn ...'",
                confidence="medium",
                score=90,
            )

    # --------------------------------------------------------
    # 23) DREAM JOB
    # --------------------------------------------------------
    if "dream job" in q_low:
        if len(a_words) >= 1 and not (a_words & yes_words | a_words & no_words):
            return result(True, "Doğru! Hayalindeki işi belirttin.", confidence="medium")
        return result(
            False,
            "Bir meslek veya iş belirtmen gerekiyor.",
            "Örneğin: 'My dream job is to be a pilot.'",
            "My dream job is to be a pilot.",
        )

    # --------------------------------------------------------
    # 24) WHERE WOULD YOU LIKE TO LIVE?
    # --------------------------------------------------------
    if "where would you like to live" in q_low:
        if has_any(a_low, {"live", "would", "like", "want"}) or place_words & a_words:
            return result(True, "Doğru! Nerede yaşamak istediğini belirttin.")
        return result(
            False,
            "Bir yer belirtmen gerekiyor.",
            "Örneğin: 'I would like to live in Istanbul.'",
            "I would like to live in Istanbul.",
        )

    # --------------------------------------------------------
    # 25) HOW ...? / METHOD
    # --------------------------------------------------------
    if q_low.startswith("how "):
        if transport_words & a_words:
            return result(True, "Doğru! Nasıl yaptığını anlattın.")

        if has_any(
            a_low,
            {"usually", "slowly", "quickly", "well", "because", "by", "can"}
        ) or len(a_words) >= 3:
            return result(
                True,
                "Doğru! Cevabın anlaşılır.",
                "",
                confidence="medium",
                score=90,
            )

    # --------------------------------------------------------
    # 26) GENERIC WHAT QUESTIONS
    # --------------------------------------------------------
    if q_low.startswith("what "):
        if len(a_words) >= 2:
            # Sadece alakasız kısa cevapları filtrele.
            invalid = {
                "yes",
                "no",
                "i am",
                "i'm",
                "okay",
                "fine",
            }
            if a_low not in invalid:
                return result(
                    True,
                    "Doğru! Cevabın sorunun istediği bilgiyi veriyor.",
                    "Cevabın anlaşılır. Daha uzun bir cümle kurarsan konuşma pratiğin daha da gelişir.",
                    confidence="medium",
                    score=90,
                )

    # --------------------------------------------------------
    # 27) HERMES SECOND-LEVEL JUDGE
    # --------------------------------------------------------
    learner_level = "A1" if st.session_state.level <= 3 else "A2"

    history_text = "\n".join(
        f"Teacher: {item['question'].get('english', '') if isinstance(item['question'], dict) else item['question']}\n"
        f"Student: {item['answer']}"
        for item in st.session_state.conversation_history[-6:]
    )

    system_prompt = (
        "You are K.A.R.T.A.L., a patient English teacher. "
        f"The learner is {learner_level}. "
        "Evaluate the student's answer ONLY against the exact current question. "
        "This is a speaking practice app, so accept natural short answers, "
        "sentence fragments that are valid in context, synonyms, contractions, "
        "and small speech-to-text mistakes. "
        "Do NOT require the student to repeat the model answer. "
        "A short answer such as 'Pizza', 'Kütahya', 'Twice a week', "
        "'No pets', or 'Rock music' can be fully correct when the question makes "
        "its meaning clear. "
        "Only mark false when the answer clearly fails to answer the question "
        "or has a serious grammar/meaning problem. "
        "If meaning is correct but grammar has a minor error, mark correct=true "
        "and explain the correction briefly. "
        "Return ONLY valid JSON with exactly these keys: "
        "correct, reply, correction, correct_answer. "
        "correct must be true or false. "
        "reply and correction must be short Turkish strings. "
        "correct_answer must be a short English sentence or empty string."
    )

    user_prompt = (
        f"Current English question: {current_question}\n"
        f"Student answer: {answer_clean}\n\n"
        f"Recent conversation:\n{history_text}"
    )

    try:
        raw = ask_ollama(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=180,
        )
        data = extract_json(raw)
    except Exception:
        data = None

    if data:
        raw_correct = data.get("correct", False)
        if isinstance(raw_correct, str):
            correct = raw_correct.strip().lower() in (
                "true", "yes", "correct", "doğru", "evet"
            )
        else:
            correct = bool(raw_correct)

        # Hermes "false" döndürse bile, iki veya daha fazla anlamlı kelimelik
        # cevapları son güvenlik katmanında tekrar kontrol et.
        if not correct and len(a_words) >= 2:
            generic_noise = {
                "yes", "no", "okay", "ok", "fine", "i", "am", "do", "not"
            }
            meaningful = a_words - generic_noise
            if len(meaningful) >= 2:
                correct = True
                data["reply"] = (
                    "Cevabın anlaşılır. Küçük bir grammar düzeltmesi olabilir."
                )

        return result(
            correct,
            str(data.get("reply", "")).strip(),
            str(data.get("correction", "")).strip(),
            str(data.get("correct_answer", "")).strip(),
            confidence="medium",
            score=90 if correct else 30,
        )

    # Hermes de kullanılamıyorsa öğrenciyi gereksiz yere cezalandırma.
    if len(a_words) >= 2:
        return result(
            True,
            "Cevabın anlaşılır görünüyor.",
            "K.A.R.T.A.L. ayrıntılı grammar kontrolü yapamadı; ancak cevabın anlamlı.",
            confidence="low",
            score=80,
        )

    return result(
        False,
        "Cevabın yeterince açık değil.",
        "Soruyu tekrar düşün ve kısa ama anlamlı bir İngilizce cevap ver.",
        confidence="low",
        score=20,
    )



# ============================================================
# K.A.R.T.A.L. ÖĞRENME MOTORU
# ============================================================

def _reset_daily_if_needed():
    from datetime import date
    today = str(date.today())
    if st.session_state.get("daily_date") != today:
        st.session_state.daily_date = today
        st.session_state.daily_progress = {"xp": 0, "questions": 0, "speaking": 0}

def record_learning_result(topic, correct, xp=0, mode="question"):
    """Konu performansını ve günlük ilerlemeyi kaydet."""
    _reset_daily_if_needed()

    topic = topic or "Genel"
    stats = st.session_state.topic_stats.setdefault(
        topic,
        {"attempts": 0, "correct": 0, "xp": 0}
    )
    stats["attempts"] += 1
    if correct:
        stats["correct"] += 1
    stats["xp"] += int(xp)

    st.session_state.daily_progress["xp"] += int(xp)
    st.session_state.daily_progress["questions"] += 1
    if mode == "speaking":
        st.session_state.daily_progress["speaking"] += 1

def topic_accuracy(topic):
    stats = st.session_state.topic_stats.get(topic, {})
    attempts = stats.get("attempts", 0)
    if attempts == 0:
        return None
    return round(100 * stats.get("correct", 0) / attempts)

def weakest_topics(limit=3):
    items = []
    for topic, stats in st.session_state.topic_stats.items():
        attempts = stats.get("attempts", 0)
        if attempts:
            accuracy = 100 * stats.get("correct", 0) / attempts
            items.append((accuracy, attempts, topic))
    items.sort(key=lambda x: (x[0], -x[1]))
    return [x[2] for x in items[:limit]]

def strongest_topics(limit=3):
    items = []
    for topic, stats in st.session_state.topic_stats.items():
        attempts = stats.get("attempts", 0)
        if attempts:
            accuracy = 100 * stats.get("correct", 0) / attempts
            items.append((accuracy, attempts, topic))
    items.sort(key=lambda x: (-x[0], -x[1]))
    return [x[2] for x in items[:limit]]

def learning_recommendation():
    weak = weakest_topics(3)
    if weak:
        return weak[0]
    return "Genel İngilizce"

def learning_goal_text():
    _reset_daily_if_needed()
    p = st.session_state.daily_progress
    g = st.session_state.daily_goal
    return (
        f"⭐ XP: {p['xp']}/{g['xp']} • "
        f"📝 Soru: {p['questions']}/{g['questions']} • "
        f"🎤 Konuşma: {p['speaking']}/{g['speaking']}"
    )

# ============================================================
# K.A.R.T.A.L. SEVİYE SİSTEMİ
# ============================================================
LEVEL_THRESHOLDS = {
    1: 0,
    2: 100,
    3: 250,
    4: 450,
    5: 700,
    6: 1000,
    7: 1400,
    8: 1850,
    9: 2400,
    10: 3000,
}

LEVEL_NAMES = {
    1: "A1 Başlangıç",
    2: "A1 Temel",
    3: "A1 Gelişiyor",
    4: "A2 Başlangıç",
    5: "A2 Temel",
    6: "A2 Gelişiyor",
    7: "B1 Başlangıç",
    8: "B1 Orta",
    9: "B1 Gelişiyor",
    10: "B2 Yolunda",
}

def kartal_level_from_xp(xp):
    current = 1
    for lvl, needed in LEVEL_THRESHOLDS.items():
        if xp >= needed:
            current = lvl
    return current

def kartal_level_progress(xp):
    lvl = kartal_level_from_xp(xp)
    if lvl >= max(LEVEL_THRESHOLDS):
        return 1.0, 0, 0
    start = LEVEL_THRESHOLDS[lvl]
    end = LEVEL_THRESHOLDS[lvl + 1]
    progress = (xp - start) / (end - start)
    return max(0.0, min(1.0, progress)), xp - start, end - xp

def kartal_question_level(xp):
    lvl = kartal_level_from_xp(xp)
    if lvl <= 3:
        return "A1"
    if lvl <= 6:
        return "A2"
    if lvl <= 9:
        return "B1"
    return "B2"

def kartal_add_xp(amount, reason=""):
    old_level = kartal_level_from_xp(st.session_state.get("xp", 0))
    st.session_state.xp = st.session_state.get("xp", 0) + int(amount)
    new_level = kartal_level_from_xp(st.session_state.xp)
    st.session_state.level = new_level

    if new_level > old_level:
        st.session_state.level_up_message = (
            f"🎉 Seviye atladın! **{new_level}. seviye — "
            f"{LEVEL_NAMES.get(new_level, 'Yeni Seviye')}**"
        )
    return new_level > old_level

# ============================================================
# HEADER
# ============================================================

st.title("🦅 K.A.R.T.A.L. English")

st.caption(
    "Yerel İngilizce Öğrenme ve Konuşma Asistanı"
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🦅 K.A.R.T.A.L.")

level, level_xp, level_target, level_progress = get_level_info()
st.sidebar.metric("⭐ XP", st.session_state.xp)
st.sidebar.metric("🏆 K.A.R.T.A.L. Seviyesi", level)
st.sidebar.progress(level_progress)
st.sidebar.caption(
    f"Seviye {level} → sonraki seviye için **{level_target - level_xp} XP**"
)
st.sidebar.write(f"🔥 Çalışma serisi: **{st.session_state.streak} gün**")

st.sidebar.divider()

menu = st.sidebar.radio(
    "Menü",
    [
        "🏠 Ana Sayfa",
        "📚 Kelime Öğren",
        "🧠 Mini Quiz",
        "✍️ Cümle Pratiği",
        "🎤 Konuşma Pratiği",
        "🤖 K.A.R.T.A.L. Konuşsun"
    ]
)

if st.session_state.get("level_up_message"):
    st.success(st.session_state.level_up_message)
    st.session_state.level_up_message = None


# ============================================================
# HOME
# ============================================================

if menu == "🏠 Ana Sayfa":

    st.header("Hoş geldiniz Patron. 🦅")

    st.write(
        "Ben K.A.R.T.A.L. "
        "İngilizce öğrenme sürecinizde size yardımcı olacağım."
    )

    level, level_xp, level_target, level_progress = get_level_info()

    st.subheader("🏆 İlerlemeniz")
    st.caption("🎯 Akıllı XP: cevap kalitesine göre +5 / +10 / +15 / +20 XP")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("⭐ Toplam XP", st.session_state.xp)
    with col2:
        st.metric("🏆 Seviye", level)
    with col3:
        st.metric(
            "🧠 Quiz Başarısı",
            f"%{get_accuracy(st.session_state.quiz_correct, st.session_state.quiz_total)}"
        )
    with col4:
        st.metric(
            "🎤 Konuşma Başarısı",
            f"%{get_accuracy(st.session_state.speaking_correct, st.session_state.speaking_attempts)}"
        )

    st.progress(level_progress)
    st.caption(
        f"Seviye {level}: **{level_xp}/{level_target} XP** • "
        f"Sonraki seviyeye {level_target - level_xp} XP kaldı."
    )

    st.divider()

    st.subheader("📊 Öğrenme İstatistikleri")
    stat1, stat2, stat3 = st.columns(3)
    with stat1:
        st.write(f"🧠 Quiz: **{st.session_state.quiz_correct}/{st.session_state.quiz_total}** doğru")
    with stat2:
        st.write(f"🎤 Konuşma: **{st.session_state.speaking_correct}/{st.session_state.speaking_attempts}** başarılı")
    with stat3:
        st.write(f"🤖 Gerçek konuşma: **{st.session_state.conversation_correct}/{st.session_state.conversation_attempts}** doğru")

    st.divider()
    st.subheader("🧠 K.A.R.T.A.L. Öğrenme Motoru")
    st.write(learning_goal_text())

    goal_xp = st.session_state.daily_goal["xp"]
    today_xp = st.session_state.daily_progress["xp"]
    st.progress(min(1.0, today_xp / max(1, goal_xp)))

    weak = weakest_topics(3)
    strong = strongest_topics(3)

    c1, c2 = st.columns(2)
    with c1:
        st.write("🔴 **Daha çok çalışılması gerekenler**")
        if weak:
            for topic in weak:
                acc = topic_accuracy(topic)
                st.write(f"• {topic} — %{acc}")
        else:
            st.caption("Henüz yeterli veri yok.")
    with c2:
        st.write("🟢 **Güçlü olduğun konular**")
        if strong:
            for topic in strong:
                acc = topic_accuracy(topic)
                st.write(f"• {topic} — %{acc}")
        else:
            st.caption("Henüz yeterli veri yok.")

    st.info(
        f"🎯 K.A.R.T.A.L. önerisi: **{learning_recommendation()}** konusuna "
        "biraz daha ağırlık ver."
    )

    st.divider()

    st.subheader("🎯 Bugünkü hedef")
    daily_goal = 100
    daily_progress = min(st.session_state.daily_xp, daily_goal) / daily_goal
    st.progress(daily_progress)
    st.write(f"Bugünkü hedef: **100 XP** • Mevcut ilerleme: **{min(st.session_state.daily_xp, 100)} XP**")

    st.write("1. 📚 Yeni kelimeler öğrenin.")
    st.write("2. 🎤 En az 5 cümleyi sesli söyleyin.")
    st.write("3. 🧠 Mini quiz çözün.")

    st.info(
        "Konuşma pratiğinde aynı cümle, "
        "cümle havuzu bitmeden tekrar gösterilmez."
    )

# ============================================================
# VOCABULARY
# ============================================================

elif menu == "📚 Kelime Öğren":

    st.header("📚 Kelime Öğren")

    level_filter = st.selectbox(
        "Seviye",
        ["Tümü", "A1", "A2"]
    )

    words = [
        x for x in LESSONS
        if level_filter == "Tümü"
        or x["level"] == level_filter
    ]

    for word in words:

        with st.container(border=True):

            col1, col2 = st.columns([2, 3])

            with col1:

                st.subheader(
                    word["word"]
                )

                st.write(
                    f"🇹🇷 {word['meaning']}"
                )

                if st.button(
                    "🔊 Dinle",
                    key=f"word_{word['word']}"
                ):

                    speak_text(
                        word["word"]
                    )

            with col2:

                st.write(
                    f"**Örnek:** {word['example']}"
                )

                if st.button(
                    "🔊 Örneği Dinle",
                    key=f"example_{word['word']}"
                ):

                    speak_text(
                        word["example"]
                    )

# ============================================================
# QUIZ
# ============================================================

elif menu == "🧠 Mini Quiz":

    st.header("🧠 Mini Quiz")

    if st.session_state.quiz_current is None:

        if st.button(
            "▶️ Quiz'e Başla",
            type="primary"
        ):

            st.session_state.quiz_current = (
                get_quiz_question()
            )

            st.rerun()

    else:

        question = st.session_state.quiz_current

        st.subheader(
            f"🇬🇧 {question['word']}"
        )

        st.write(
            "Türkçe anlamı nedir?"
        )

        options = [
            question["meaning"]
        ]

        other_words = [
            x["meaning"]
            for x in LESSONS
            if x["meaning"] != question["meaning"]
        ]

        random.shuffle(other_words)

        options.extend(
            other_words[:3]
        )

        random.shuffle(options)

        answer = st.radio(
            "Cevap",
            options,
            key=f"quiz_answer_{question['word']}"
        )

        if st.button(
            "Cevabı Kontrol Et",
            type="primary"
        ):

            st.session_state.quiz_total += 1

            if answer == question["meaning"]:

                st.success(
                    "✅ Doğru cevap!"
                )

                st.session_state.quiz_score += 1
                st.session_state.quiz_correct += 1
                register_activity()

                add_xp(10)

                speak_text(
                    "Correct! Very good!"
                )

            else:

                register_activity()
                st.error(
                    f"❌ Yanlış. Doğru cevap: "
                    f"{question['meaning']}"
                )

                speak_text(
                    f"The correct answer is {question['meaning']}"
                )

            st.session_state.quiz_current = None

            st.rerun()

    if st.session_state.quiz_total > 0:

        st.divider()

        st.write(
            f"Skor: "
            f"**{st.session_state.quiz_score}/"
            f"{st.session_state.quiz_total}**"
        )

# ============================================================
# SENTENCE PRACTICE
# ============================================================

elif menu == "✍️ Cümle Pratiği":

    st.header("✍️ Cümle Pratiği")

    st.write(
        "İngilizce cümleyi okuyun ve anlamını öğrenin."
    )

    if "practice_sentence" not in st.session_state:

        st.session_state.practice_sentence = (
            random.choice(SPEAKING_SENTENCES)
        )

    sentence = st.session_state.practice_sentence

    st.markdown(
        f"### 🇬🇧 {sentence['english']}"
    )

    st.write(
        f"🇹🇷 **{sentence['turkish']}**"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔊 İngilizce Dinle",
            type="primary"
        ):

            speak_text(
                sentence["english"]
            )

    with col2:

        if st.button(
            "🔄 Yeni Cümle"
        ):

            st.session_state.practice_sentence = (
                random.choice(SPEAKING_SENTENCES)
            )

            st.rerun()

# ============================================================
# SPEAKING PRACTICE
# ============================================================

elif menu == "🎤 Konuşma Pratiği":

    st.header("🎤 Konuşma Pratiği")

    st.write(
        "Cümleyi dinleyin, sonra mikrofona İngilizce söyleyin."
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    categories = [
        "Tümü"
    ] + sorted(
        list(
            set(
                x["category"]
                for x in SPEAKING_SENTENCES
            )
        )
    )

    levels = [
        "Tümü",
        "A1",
        "A2"
    ]

    col1, col2 = st.columns(2)

    with col1:

        selected_category = st.selectbox(
            "Kategori",
            categories
        )

    with col2:

        selected_level = st.selectbox(
            "Seviye",
            levels
        )

    # --------------------------------------------------------
    # FILTER CHANGE RESET
    # --------------------------------------------------------

    filter_key = (
        selected_category,
        selected_level
    )

    if "last_filter_key" not in st.session_state:

        st.session_state.last_filter_key = filter_key

    elif (
        st.session_state.last_filter_key
        != filter_key
    ):

        st.session_state.speaking_queue = []
        st.session_state.current_sentence = None
        st.session_state.last_filter_key = filter_key

    # --------------------------------------------------------
    # NEW SENTENCE
    # --------------------------------------------------------

    if st.session_state.current_sentence is None:

        st.session_state.current_sentence = (
            get_next_sentence(
                selected_category,
                selected_level
            )
        )

    sentence = st.session_state.current_sentence

    if sentence is None:

        st.warning(
            "Bu filtrede cümle bulunamadı."
        )

    else:

        st.markdown(
            f"## 🇬🇧 {sentence['english']}"
        )

        st.caption(
            f"Kategori: {sentence['category']} "
            f"| Seviye: {sentence['level']}"
        )

        with st.expander(
            "🇹🇷 Türkçe anlamını göster"
        ):

            st.write(
                sentence["turkish"]
            )

        # ----------------------------------------------------
        # LISTEN
        # ----------------------------------------------------

        if st.button(
            "🔊 Cümleyi Dinle",
            type="primary"
        ):

            speak_text(
                sentence["english"]
            )

        st.divider()

        # ----------------------------------------------------
        # MICROPHONE
        # ----------------------------------------------------

        st.subheader(
            "🎙️ Şimdi siz söyleyin"
        )

        audio = st.audio_input(
            "Mikrofonu aç ve cümleyi söyle"
        )

        if audio:

            with st.spinner(
                "🎧 Konuşmanız analiz ediliyor..."
            ):

                spoken_text = transcribe_audio(
                    audio
                )

            if spoken_text:

                audio_hash = hashlib.sha256(audio.getvalue()).hexdigest()
                is_new_attempt = audio_hash != st.session_state.last_speech_audio_hash
                if is_new_attempt:
                    st.session_state.last_speech_audio_hash = audio_hash
                    st.session_state.speaking_attempts += 1
                    register_activity()

                st.write(
                    f"🗣️ **Sizin söylediğiniz:** "
                    f"{spoken_text}"
                )

                score = speech_score(
                    sentence["english"],
                    spoken_text
                )

                st.progress(
                    score / 100
                )

                st.metric(
                    "Konuşma skoru",
                    f"%{score}"
                )

                if score >= 90:

                    st.success(
                        "🏆 Mükemmel! Telaffuz ve cümle çok iyi."
                    )

                    speak_text(
                        "Excellent! Very good!"
                    )

                    if is_new_attempt:
                        st.session_state.speaking_correct += 1
                    add_xp(20, "Konuşma: mükemmel telaffuz")

                elif score >= 70:

                    if is_new_attempt:
                        st.session_state.speaking_correct += 1
                    st.success(
                        "👏 Çok iyi! Biraz daha pratik yaparsanız mükemmel olacak."
                    )

                    speak_text(
                        "Very good! Keep practicing."
                    )

                    add_xp(10, "Konuşma: çok iyi")

                elif score >= 50:

                    st.warning(
                        "👍 Fena değil. Birkaç kez daha deneyin."
                    )

                    speak_text(
                        "Good try. Please practice again."
                    )

                    add_xp(5, "Konuşma: geliştirilebilir")

                else:

                    st.error(
                        "🔁 Biraz daha çalışalım. Cümleyi tekrar dinleyin ve yeniden söyleyin."
                    )

                    speak_text(
                        "Let's try again. Listen carefully and repeat."
                    )

            else:

                st.error(
                    "Konuşma algılanamadı. "
                    "Mikrofonu kontrol edip tekrar deneyin."
                )

        st.divider()

        # ----------------------------------------------------
        # NEXT
        # ----------------------------------------------------

        remaining = len(
            st.session_state.speaking_queue
        )

        st.write(
            f"📦 Bu turda kalan cümle: **{remaining}**"
        )

        if st.button(
            "➡️ Yeni Cümle",
            type="primary"
        ):

            st.session_state.current_sentence = (
                get_next_sentence(
                    selected_category,
                    selected_level
                )
            )

            st.rerun()

# ============================================================
# KARTAL TALKS
# ============================================================

elif menu == "🤖 K.A.R.T.A.L. Konuşsun":

    st.header("🤖 K.A.R.T.A.L. Gerçek Konuşma")

    st.write(
        "K.A.R.T.A.L. artık hazır cevaplarla sınırlı değil. "
        "Seviyenize uygun sorular seçip cevabınızı değerlendirerek konuşmayı sürdürüyor."
    )

    learner_level = _target_cefr_level()
    st.info(f"🎯 Mevcut İngilizce seviyesi: **{learner_level}** • Sorular seviyene göre otomatik seçiliyor. • Önerilen konu: **{learning_recommendation()}**")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "▶️ Konuşmayı Başlat",
            type="primary",
            use_container_width=True,
        ):
            try:
                with st.spinner("🧠 K.A.R.T.A.L. soruyu hazırlıyor..."):
                    question = generate_conversation_question()

                st.session_state.conversation_history = []
                st.session_state.conversation_used_questions = [question["english"]]
                st.session_state.conversation_question = question
                st.session_state.conversation_last_answer = ""
                st.session_state.conversation_started = True

                speak_text(question["english"])
                st.rerun()

            except Exception as e:
                st.error(str(e))
                st.code(
                    "ollama list\nollama run hermes3:3b",
                    language="powershell",
                )

    with col2:
        if st.button(
            "⏹️ Konuşmayı Sıfırla",
            use_container_width=True,
        ):
            st.session_state.conversation_history = []
            st.session_state.conversation_used_questions = []
            st.session_state.conversation_question = None
            st.session_state.conversation_last_answer = ""
            st.session_state.conversation_started = False
            st.rerun()

    if not st.session_state.conversation_started:

        st.divider()

        st.markdown(
            """
            ### 🦅 Nasıl çalışıyor?

            1. K.A.R.T.A.L. İngilizce bir soru sorar.
            2. Soruyu sesli olarak dinlersiniz.
            3. Mikrofondan İngilizce cevap verirsiniz.
            4. Whisper cevabınızı yazıya çevirir.
            5. K.A.R.T.A.L. cevabınızı değerlendirir.
            6. Yanlışsa K.A.R.T.A.L. hatanızı Türkçe açıklar.
            7. Doğru İngilizce cevabı gösterir ve telaffuzunu sesli söyler.
            8. Doğru cevapta otomatik olarak sonraki soruya geçer.
            """
        )

        st.warning("Başlamak için **Konuşmayı Başlat** düğmesine basın.")

    else:

        question = normalize_conversation_question(
            st.session_state.conversation_question
        )
        st.session_state.conversation_question = question

        st.divider()
        st.subheader("🦅 K.A.R.T.A.L. soruyor")
        st.markdown(f"### 🇬🇧 {question['english']}")
        st.caption(f"📚 Soru seviyesi: **{question.get('level', _target_cefr_level())}**")
        if question.get("turkish"):
            st.info(f"🇹🇷 **Türkçesi:** {question['turkish']}")

        if st.button(
            "🔊 Soruyu Tekrar Dinle",
            key="repeat_conversation_question",
        ):
            speak_text(question["english"])

        st.subheader("🎙️ Cevabınızı söyleyin")

        audio = st.audio_input("Mikrofonu aç ve İngilizce cevap ver")

        if audio:

            with st.spinner("🎧 K.A.R.T.A.L. sizi dinliyor..."):
                spoken = transcribe_audio(audio)

            if spoken:

                st.write(f"🗣️ **Siz:** {spoken}")

                if spoken.strip() == st.session_state.conversation_last_answer.strip():
                    st.info("Bu cevap zaten işlendi. Yeni bir cevap söyleyin.")

                else:

                    audio_hash = hashlib.sha256(audio.getvalue()).hexdigest()
                    if audio_hash == st.session_state.last_conversation_audio_hash:
                        st.info("Bu kayıt zaten işlendi. Yeni bir cevap söyleyin.")
                        st.stop()

                    st.session_state.last_conversation_audio_hash = audio_hash
                    st.session_state.conversation_last_answer = spoken

                    try:
                        with st.spinner(
                            "🧠 Hermes 3B cevabınızı değerlendiriyor..."
                        ):
                            result = evaluate_conversation_answer(
                                question,
                                spoken,
                            )

                        reply = result["reply"]
                        correction = result["correction"]
                        next_question = result["next_question"]
                        evaluation_score = result.get("score", 100)
                        evaluation_confidence = result.get("confidence", "high")

                        st.session_state.conversation_attempts += 1
                        register_activity()
                        is_correct = result.get("correct", False)
                        if is_correct:
                            st.session_state.conversation_correct += 1

                        conv_topic = (
                            question.get("category")
                            or question.get("topic")
                            or "Konuşma"
                        )
                        record_learning_result(
                            conv_topic,
                            is_correct,
                            evaluation_score if is_correct else 0,
                            mode="speaking",
                        )

                        st.session_state.conversation_history.append(
                            {
                                "question": question,
                                "answer": spoken,
                            }
                        )

                        # Cevap kalitesine göre 0/5/10/15/20 XP ver.
                        if result.get("correct", False):
                            gained_xp, xp_reason = smart_xp_from_score(
                                evaluation_score,
                                correct=True,
                            )
                            add_xp(gained_xp, xp_reason)

                            st.success(
                                f"✅ {reply or 'Doğru cevap!'}"
                            )
                            st.caption(
                                f"🎯 Cevap değerlendirmesi: %{evaluation_score} "
                                f"• Güven: {evaluation_confidence}"
                            )
                            if gained_xp > 0:
                                st.info(
                                    f"{xp_reason} — **+{gained_xp} XP** kazandın!"
                                )

                            level_now, level_xp_now, level_target_now, _ = get_level_info()
                            if level_xp_now >= 80 and level_now < 1000:
                                st.warning(
                                    f"🔥 Seviye {level_now} bitmek üzere! "
                                    f"Sonraki seviyeye **{level_target_now - level_xp_now} XP** kaldı."
                                )

                            # ÖNEMLİ: Öğrencinin cevabını K.A.R.T.A.L. SESLENDİRMEZ.
                            # Sadece yeni soruyu seslendirir.
                            if (
                                not isinstance(next_question, dict)
                                or not next_question.get("english")
                            ):
                                next_question = generate_conversation_question()

                            st.session_state.conversation_question = next_question

                            speak_text(next_question["english"])
                            st.rerun()

                        else:
                            # Yanlış cevapta aynı soruda kal.
                            # Türkçe hata açıklaması ekranda gösterilir.
                            st.error(
                                f"❌ {reply or 'Cevabınız henüz doğru değil.'}"
                            )

                            if correction:
                                st.warning(
                                    f"🇹🇷 **Nerede yanlış yaptınız?**\n\n{correction}"
                                )

                            correct_answer = result.get("correct_answer", "")
                            if correct_answer:
                                st.info(
                                    f"🇬🇧 **Doğru İngilizce cevap:** {correct_answer}"
                                )

                                # Yanlış cevapta K.A.R.T.A.L. doğru cevabı
                                # otomatik olarak İngilizce seslendirir.
                                st.caption("🔊 K.A.R.T.A.L. doğru cevabın telaffuzunu söylüyor...")
                                speak_text(correct_answer)

                                if st.button(
                                    "🔊 Doğru cevabı tekrar dinle",
                                    key=f"repeat_correct_answer_{len(st.session_state.conversation_history)}",
                                ):
                                    speak_text(correct_answer)

                            st.info(
                                "🔁 Aynı soruyu tekrar cevaplayın. Doğru cevap verdiğinizde K.A.R.T.A.L. otomatik olarak sonraki soruya geçecek."
                            )

                    except Exception as e:

                        st.error(str(e))
                        st.code(
                            "ollama list\nollama run hermes3:3b",
                            language="powershell",
                        )

            else:

                st.error(
                    "Konuşma algılanamadı. "
                    "Mikrofonu kontrol edip tekrar deneyin."
                )

        st.divider()

        st.subheader("📚 Konuşma Geçmişi")

        if st.session_state.conversation_history:

            for i, item in enumerate(
                st.session_state.conversation_history,
                1,
            ):

                with st.container(border=True):

                    old_q = item["question"]
                    old_q_text = (
                        old_q.get("english", "")
                        if isinstance(old_q, dict)
                        else str(old_q)
                    )
                    st.write(
                        f"**{i}. K.A.R.T.A.L.:** {old_q_text}"
                    )

                    st.write(f"**Siz:** {item['answer']}")

        else:

            st.caption("Henüz konuşma geçmişi yok.")

        st.divider()

        st.caption(
            "🧠 Zekâ: Ollama / Hermes 3B  •  "
            "🎤 Ses tanıma: faster-whisper  •  "
            "🔊 Ses: Windows TTS / Cloud TTS"
        )

# ============================================================
# BULUT SES OYNATICI
# ============================================================

if st.session_state.get("tts_audio"):
    st.audio(
        st.session_state.tts_audio,
        format="audio/mp3",
        autoplay=True,
    )
    st.caption(f"🔊 K.A.R.T.A.L. ses: {st.session_state.get('tts_audio_text', '')}")

# ============================================================
# FOOTER
# ============================================================

st.sidebar.divider()

st.sidebar.caption(
    "K.A.R.T.A.L. English"
)

st.sidebar.caption(
    "XP • Seviye • İstatistikler • Whisper • Cloud TTS"
)