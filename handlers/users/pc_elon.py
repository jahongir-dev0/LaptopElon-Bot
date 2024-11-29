from keyboards.inline.check_elon import check, check_admin
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.types import Message
from states.elonState import PcElonState
from keyboards.default.pc_elon import menu
from data.config import ADMINS

@dp.message_handler(text = "Kompyuter sotuv kanali 💻")
async def one(message: Message):
    await message.answer("Kanalga Kirish Uchun Quyidagi Linkga Bosing 👉 @pc_elon")

@dp.message_handler(text = "Elon berish!")
async def one(message: Message):
    await message.answer("🖼Noutbukning rasmini yuboring!")
    await PcElonState.rasm.set()
    
@dp.message_handler(content_types='photo', state = PcElonState.rasm)
async def two(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    
    await state.update_data({
        'rasm':photo
    })
    
    await message.answer("Iltimos Noutbukning markasini kiriting\nMasalan: Lenovo yoki Acer")
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.nomi)
async def three(message: Message, state: FSMContext):
    nom = message.text
    
    await state.update_data({
        "nomi":nom
    })
    
    await message.answer("Bu noutbukni asosan qanday ishlarga ishlatish mumkin\nMasalan: Ofis ishlari yoki Gaming")
    await PcElonState.next()
    
    
@dp.message_handler(state= PcElonState.qanaqa_ish_uchun)
async def four(message: Message, state: FSMContext):
    ish = message.text
    
    await state.update_data({
        "qanaqa_ish_uchun":ish
    })
    
    await message.answer("Noutbukning holatini kiriting!\nMasalan: Yangi, Ozroq ishlatilgan, Ideal, Udar, Qirilgan joyi lekin yangi")
    await PcElonState.next()
    


@dp.message_handler(state = PcElonState.holat)
async def five(message: Message, state: FSMContext):
    holat = message.text
    
    await state.update_data({
        "holat":holat
    })
    
    
    await message.answer("Ekran razmerini kiriting:\nMasalan:15.6 dyuym HD, 17 dyuym Full HD")
    
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.ekrani)
async def six(message: Message, state: FSMContext):
    ekran = message.text
    
    await state.update_data({
        "ekrani":ekran
    })
    
    await message.answer("Protsessorini kiriting:\nMasalan:Intel Core i5 10 pokoleniya")
    await PcElonState.next()
    
    
@dp.message_handler(state=PcElonState.protsessori)
async def seven(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "protsessori":name
    })
    
    await message.answer("Noutbukning xotirasini kiriting:\nMasalan: 128gb SSD va 520gb HDD")
    
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.xotirasi)
async def eight(message: Message, state:FSMContext):
    name = message.text
    
    await state.update_data({
        "xotirasi":name
    })
    
    await message.answer("Noutbukning operativkasini kiriting:\nMasalan: 8gb DDR4, 4gb DDR3")
    
    await PcElonState.next()
    
@dp.message_handler(state = PcElonState.operativkasi)
async def nine(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "operativkasi":name
    })
    
    await message.answer("Noutbukning videokartasini kiriting:\nAgar videokartasi bo'lmasa shunchaki INTEGRATED\nMasalan Intel HD Graphics 2gb")
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.videokartasi)
async def ten(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "videokartasi":name
    })
    
    await message.answer("Noutbukning batareyasi necha soatga yetishini kiriting\nMasalan: 5 soat yoki zaryad ushlamaydi")
    
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.batareyasi)
async def eleven(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "batareyasi":name
    })
    
    
    await message.answer("Qayerda joylashganligingizni kiriting\nMasalan: Jizzax, Toshkent yoki Samarqand")
    await PcElonState.next()
    
    
@dp.message_handler(state = PcElonState.joy)
async def twelve(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "joy":name
    })
    
    await message.answer("Noutbuk narxini kiriting:\nMasalan 200$ yoki 2 000 000 so'm")
    await PcElonState.next()
    
    
    
    
@dp.message_handler(state = PcElonState.narx)
async def thirteen(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        "narx":name,
        
    })
    
    await message.answer("Endi telefon raqamingiz iloji borija to'g'ri yozing chunki mijozlar ushbu raqamga bog'lanishadi!")
    await PcElonState.next()
    
@dp.message_handler(state = PcElonState.telefon)
async def fourteen(message: Message, state: FSMContext):
    numer = message.text
    
    await state.update_data({
        "telefon":numer
    })
    
    data = await state.get_data()
    rasm = f"{data['rasm']}"
    telegram = message.from_user.username
    if telegram:
        caption = f"💻{data['nomi']}\n"
        caption += f"🖥Ekran: {data['ekrani']}\n"
        caption += f"⚙️Protsessori: {data['protsessori']}\n"
        caption += f"🖲 Videokartasi: {data['videokartasi']}\n"
        caption += f"⏳ Operativka: {data['operativkasi']}\n"
        caption += f"💾 Xotirasi: {data['xotirasi']}\n"
        caption += f"🔋 Batareykasi: {data['batareyasi']}\n"
        caption += f"📌 {data['qanaqa_ish_uchun']}\n"
        caption += f"💬 Holati: {data['holat']}\n"
        caption += f"💵 Narxi: {data['narx']}\n"
        caption += f"📍 Manzil: {data['joy']}\n"
        caption += f"📥 Telegram: @{telegram}\n"
        caption += f"☎️ Telefon: {data['telefon']}\n"
    else:
     
        caption = f"💻{data['nomi']}\n"
        caption += f"🖥Ekran: {data['ekrani']}\n"
        caption += f"⚙️Protsessori: {data['protsessori']}\n"
        caption += f"🖲 Videokartasi: {data['videokartasi']}\n"
        caption += f"⏳ Operativka: {data['operativkasi']}\n"
        caption += f"💾 Xotirasi: {data['xotirasi']}\n"
        caption += f"🔋 Batareykasi: {data['batareyasi']}\n"
        caption += f"📌 {data['qanaqa_ish_uchun']}\n"
        caption += f"💬 Holati: {data['holat']}\n"
        caption += f"💵 Narxi: {data['narx']}\n"
        caption += f"📍 Manzil: {data['joy']}\n"
        caption += f"☎️ Telefon: {data['telefon']}\n"
    await message.answer_photo(photo = rasm, caption=caption)    
    await message.answer("Barcha malumotlar to'g'rimi?",reply_markup=check)
    
    await PcElonState.next()
   
@dp.message_handler(state = PcElonState.check)
async def fiveteen(message: Message, state: FSMContext):
    matn = message.text
    if matn == "Yuborish":
        data = await state.get_data()
        rasm = f"{data['rasm']}"
        telegram = message.from_user.get_mention()
        await message.answer("Adminga Yuborildi✅")
        
        caption = f"💻{data['nomi']}\n"
        caption += f"🖥Ekran: {data['ekrani']}\n"
        caption += f"⚙️Protsessori: {data['protsessori']}\n"
        caption += f"🖲 Videokartasi: {data['videokartasi']}\n"
        caption += f"⏳ Operativka: {data['operativkasi']}\n"
        caption += f"💾 Xotirasi: {data['xotirasi']}\n"
        caption += f"🔋 Batareykasi: {data['batareyasi']}\n"
        caption += f"📌 {data['qanaqa_ish_uchun']}\n"
        caption += f"💬 Holati: {data['holat']}\n"
        caption += f"💵 Narxi: {data['narx']}\n"
        caption += f"📍 Manzil: {data['joy']}\n"
        caption += f"📥 Telegram::️ {telegram}\n"
        caption += f"☎️ Telefon: {data['telefon']}\n"            
        
        await bot.send_photo(chat_id=6483758367, photo = rasm, caption=caption, reply_markup=check_admin)
        await PcElonState.next()
    else:
        await message.answer("Elon bekor qilindi", reply_markup=menu)
        await state.finish()

# @dp.message_handler(text_contains = "Kanalga joylash")
# async def send_channel(message: Message):
#     await bot.send_photo(chat_id = -1001811158613, photo = rasm, caption = caption)
        
@dp.message_handler(text_contains = "Kanalga joylash", state=PcElonState.check_admin)
async def sixteen(message: Message, state: FSMContext):
    data = await state.get_data()
    rasm = f"{data['rasm']}"
    telegram = message.from_user.get_mention()
    
    caption = f"💻{data['nomi']}\n"
    caption += f"🖥Ekran: {data['ekrani']}\n"
    caption += f"⚙️Protsessori: {data['protsessori']}\n"
    caption += f"🖲 Videokartasi: {data['videokartasi']}\n"
    caption += f"⏳ Operativka: {data['operativkasi']}\n"
    caption += f"💾 Xotirasi: {data['xotirasi']}\n"
    caption += f"🔋 Batareykasi: {data['batareyasi']}\n"
    caption += f"📌 {data['qanaqa_ish_uchun']}\n"
    caption += f"💬 Holati: {data['holat']}\n"
    caption += f"💵 Narxi: {data['narx']}\n"
    caption += f"📍 Manzil: {data['joy']}\n"
    caption += f"📥 Telegram:➡️ {telegram}\n"
    caption += f"☎️ Telefon: {data['telefon']}\n"

    await bot.send_photo(chat_id = -1002332951281, photo = rasm, caption=caption)
    await state.finish()