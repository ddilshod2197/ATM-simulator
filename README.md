# Bank Hisob Simulyatori

Bu dastur foydalanuvchiga virtual bank hisobini boshqarishga yordam beradi. PIN autentifikatsiyasi, balansni tekshirish, pul qo'yish, pul yechish va inputlarni tekshirish kabi xususiyatlarni o'z ichiga oladi.

## Asosiy Xususiyatlar

- **PIN orqali autentifikatsiya**: Hisobga kirish uchun PIN kodi talab qilinadi.
- **Balansni tekshirish**: Hisobdagi mavjud mablag'ni ko'rish.
- **Pul qo'yish**: Hisobga pul qo'yish imkoniyati.
- **Pul yechish**: Hisobdan pul yechish, balansni tekshirish.
- **Xatolarni boshqarish**: Musbat miqdorlar va etarli mablag' bilan ishlash.

## Talablar

- Python 3.x

## O'rnatish va Ishlatish

1. **Reponi klonlash**:
   ```bash
   git clone https://github.com/your-username/bank-account-simulator.git
````

2. **Loyihaga kirish**:

   ```bash
   cd bank-account-simulator
   ```

3. **Dastur ishlatish**:
   Python o'rnatilgan bo'lsa, quyidagi buyruqni bajarib, dasturdan foydalaning:

   ```bash
   python bank_account_simulator.py
   ```

## Foydalanish

1. **PIN orqali autentifikatsiya**:
   Dastur boshlanishida PIN kiritish so'raladi. Standart PIN: `1234`.
   3 ta noto'g'ri urinishdan keyin kirish bloklanadi.

2. **Menudagi Tanlovlar**:
   PIN to'g'ri kiritilgandan so'ng, foydalanuvchiga quyidagi imkoniyatlar taqdim etiladi:

   * **Balansni tekshirish**: Hisobdagi jami mablag'ni ko'rish.
   * **Pul qo'yish**: Hisobga pul qo'yish.
   * **Pul yechish**: Hisobdan pul yechish (balansni tekshiradi).
   * **Chiqish**: Dasturdan chiqish.

### Namuna

```
Bankomat Simulyatori. Standart PIN: 1234
PIN kiriting: ****
1) Balans  2) Pul qo'yish  3) Pul yechish  4) Chiqish
Tanlov: 1
Balans: 100000 so'm
```

## Xatolarni Boshqarish

* **Noto'g'ri PIN**: 3 ta noto'g'ri PIN urinishidan so'ng kirish bloklanadi.
* **Yaroqsiz miqdorlar**: Faqat musbat miqdorlar qabul qilinadi. Salbiy yoki nol miqdor kiritish mumkin emas.
* **Balans yetishmasligi**: Pul yechish so'rovi balansdan ortiqcha bo'lsa, dastur xato haqida ogohlantiradi.

## Litsenziya

Ushbu loyiha MIT Litsenziyasi ostida litsenziyalanadi — batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'ring.

