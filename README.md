# Educational Website 🎓

A comprehensive educational platform built with Django that allows users to access courses, track their progress, and learn through embedded video content.

## ✨ Features

- 🔐 User Authentication (Register/Login)
- 📊 Personalized Dashboard
- 📚 Course Management
- 📈 Progress Tracking
- 🎥 Video Lessons
- 📱 Firebase Analytics Integration
- 🌙 Dark Mode Design
- 🔒 Content Protection
- 🛡️ AdBlock Detection
- 🌍 Multi-language Support (English, Persian)
- 📱 Responsive Design
- 🔍 Advanced Course Search
- 💬 Student-Teacher Interaction

## 🧠 Technical Architecture

### Backend Framework
- **Django 4.2**: Core web framework
- **Django ORM**: Database interaction layer
- **Crispy Forms + Bootstrap5**: Form rendering
- **Django Rosetta**: Translation management

### Frontend Technologies
- **Bootstrap 5**: CSS framework for responsive design
- **JavaScript/jQuery**: Client-side interactions
- **HTML5/CSS3**: Markup and styling
- **Dark Mode Toggle**: Custom implementation

### Database Models
- **User**: Extended Django user model with profile information
- **Course**: Main course content and metadata
- **Lesson**: Individual lessons within courses
- **Progress**: User completion tracking
- **Enrollment**: User-course relationships
- **Categories**: Course categorization system

### Authentication System
- **Django Authentication**: Core authentication
- **Email Verification**: Custom implementation
- **Firebase Auth Integration**: Optional OAuth

### Storage
- **Local Media Storage**: Development environment
- **Cloud Storage**: Production environment
- **WhiteNoise**: Static file serving

## 🚀 Setup Instructions

1. 📥 Clone the repository
2. 🛠️ Create a virtual environment:
   ```
   python -m venv venv
   ```
3. ▶️ Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. 📦 Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. 🗃️ Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. 👤 Create a superuser:
   ```
   python manage.py createsuperuser
   ```
7. 🖥️ Run the development server:
   ```
   python manage.py runserver
   ```

## 🏗️ Project Structure

- `accounts`: User authentication and management
  - Custom user models
  - Profile management
  - Authentication views
  - Email verification
- `courses`: Course and lesson management
  - Course models and views
  - Lesson content
  - Progress tracking
  - Content protection
- `dashboard`: User dashboard and progress tracking
  - User statistics
  - Course progress
  - Recommendations
- `core`: Static pages and common functionality
  - Homepage
  - About pages
  - Contact forms
  - Site-wide templates

## 💻 Technologies Used

- **Django**: Web framework
- **Bootstrap**: Frontend framework
- **PostgreSQL**: Production database
- **SQLite**: Development database
- **Firebase Analytics**: User behavior tracking
- **WhiteNoise**: Static file serving
- **Gunicorn**: WSGI HTTP Server
- **Python-dotenv**: Environment management
- **Django Crispy Forms**: Form rendering
- **Django Rosetta**: Translation interface

## 🔒 Security Features

- CSRF Protection
- XSS Prevention
- Content Security Policy
- Secure Cookie Configuration
- Password Validation Rules
- Rate Limiting on Auth Endpoints
- Content Protection for Paid Courses

## 🌐 API and Integrations

- **Firebase**: Analytics and Authentication
- **Email Service**: SMTP Integration
- **RESTful API**: For mobile app (future)

## 🚀 Deployment on Render

1. Sign up for Render: https://render.com
2. Connect your GitHub repository
3. Create a new Web Service:
   - Environment: Python
   - Build Command: `./build.sh`
   - Start Command: `gunicorn edusite.wsgi:application --log-file -`
4. Add environment variables from `env.sample`
5. Set up PostgreSQL database
6. Deploy your application

## 🔮 Future Roadmap

- Mobile Application
- Payment Gateway Integration
- Live Session Features
- Certificate Generation
- Gamification Elements
- Advanced Analytics Dashboard
- API for Third-party Integrations

---

<div dir="rtl">

# وب‌سایت آموزشی 🎓

یک پلتفرم آموزشی جامع که با Django ساخته شده است و به کاربران امکان دسترسی به دوره‌ها، پیگیری پیشرفت‌شان و یادگیری از طریق محتوای ویدیویی را می‌دهد.

## ✨ ویژگی‌ها

- 🔐 احراز هویت کاربر (ثبت‌نام/ورود)
- 📊 داشبورد شخصی‌سازی شده
- 📚 مدیریت دوره
- 📈 پیگیری پیشرفت
- 🎥 دروس ویدیویی
- 📱 یکپارچه‌سازی با Firebase Analytics
- 🌙 طراحی حالت تاریک
- 🔒 محافظت از محتوا
- 🛡️ تشخیص AdBlock
- 🌍 پشتیبانی چند زبانه (انگلیسی، فارسی)
- 📱 طراحی واکنش‌گرا
- 🔍 جستجوی پیشرفته دوره
- 💬 تعامل دانش‌آموز-معلم

## 🧠 معماری فنی

### فریم‌ورک بک‌اند
- **Django 4.2**: فریم‌ورک اصلی وب
- **Django ORM**: لایه تعامل با پایگاه داده
- **Crispy Forms + Bootstrap5**: رندر فرم‌ها
- **Django Rosetta**: مدیریت ترجمه

### فناوری‌های فرانت‌اند
- **Bootstrap 5**: فریم‌ورک CSS برای طراحی واکنش‌گرا
- **JavaScript/jQuery**: تعامل‌های سمت کلاینت
- **HTML5/CSS3**: نشانه‌گذاری و استایل‌دهی
- **تغییر حالت تاریک**: پیاده‌سازی سفارشی

### مدل‌های پایگاه داده
- **کاربر**: مدل کاربر Django با اطلاعات پروفایل
- **دوره**: محتوای اصلی دوره و متادیتا
- **درس**: دروس فردی در دوره‌ها
- **پیشرفت**: پیگیری تکمیل کاربر
- **ثبت‌نام**: روابط کاربر-دوره
- **دسته‌بندی‌ها**: سیستم طبقه‌بندی دوره

### سیستم احراز هویت
- **احراز هویت Django**: احراز هویت اصلی
- **تأیید ایمیل**: پیاده‌سازی سفارشی
- **یکپارچه‌سازی با Firebase Auth**: OAuth اختیاری

### ذخیره‌سازی
- **ذخیره‌سازی رسانه محلی**: محیط توسعه
- **ذخیره‌سازی ابری**: محیط تولید
- **WhiteNoise**: سرویس فایل‌های استاتیک

## 🚀 دستورالعمل‌های راه‌اندازی

1. 📥 مخزن را کلون کنید
2. 🛠️ یک محیط مجازی ایجاد کنید:
   ```
   python -m venv venv
   ```
3. ▶️ محیط مجازی را فعال کنید:
   - ویندوز: `.\venv\Scripts\activate`
   - لینوکس/مک: `source venv/bin/activate`
4. 📦 وابستگی‌ها را نصب کنید:
   ```
   pip install -r requirements.txt
   ```
5. 🗃️ مهاجرت‌ها را اجرا کنید:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. 👤 یک کاربر ارشد ایجاد کنید:
   ```
   python manage.py createsuperuser
   ```
7. 🖥️ سرور توسعه را اجرا کنید:
   ```
   python manage.py runserver
   ```

## 🏗️ ساختار پروژه

- `accounts`: احراز هویت و مدیریت کاربر
  - مدل‌های کاربر سفارشی
  - مدیریت پروفایل
  - نماهای احراز هویت
  - تأیید ایمیل
- `courses`: مدیریت دوره و درس
  - مدل‌ها و نماهای دوره
  - محتوای درس
  - پیگیری پیشرفت
  - محافظت از محتوا
- `dashboard`: داشبورد کاربر و پیگیری پیشرفت
  - آمار کاربر
  - پیشرفت دوره
  - توصیه‌ها
- `core`: صفحات استاتیک و عملکرد عمومی
  - صفحه اصلی
  - صفحات درباره ما
  - فرم‌های تماس
  - قالب‌های سراسری سایت

## 💻 فناوری‌های مورد استفاده

- **Django**: فریم‌ورک وب
- **Bootstrap**: فریم‌ورک فرانت‌اند
- **PostgreSQL**: پایگاه داده تولید
- **SQLite**: پایگاه داده توسعه
- **Firebase Analytics**: ردیابی رفتار کاربر
- **WhiteNoise**: سرویس فایل‌های استاتیک
- **Gunicorn**: سرور HTTP WSGI
- **Python-dotenv**: مدیریت محیط
- **Django Crispy Forms**: رندر فرم
- **Django Rosetta**: رابط ترجمه

## 🔒 ویژگی‌های امنیتی

- محافظت CSRF
- جلوگیری از XSS
- سیاست امنیتی محتوا
- پیکربندی کوکی امن
- قوانین اعتبارسنجی رمز عبور
- محدودیت نرخ در نقاط پایانی احراز هویت
- محافظت از محتوا برای دوره‌های پرداختی

## 🌐 API و یکپارچه‌سازی‌ها

- **Firebase**: تجزیه و تحلیل و احراز هویت
- **سرویس ایمیل**: یکپارچگی SMTP
- **API RESTful**: برای اپلیکیشن موبایل (آینده)

## 🚀 استقرار در Render

1. در Render ثبت‌نام کنید: https://render.com
2. مخزن GitHub خود را متصل کنید
3. یک سرویس وب جدید ایجاد کنید:
   - محیط: Python
   - دستور ساخت: `./build.sh`
   - دستور شروع: `gunicorn edusite.wsgi:application --log-file -`
4. متغیرهای محیطی را از `env.sample` اضافه کنید
5. پایگاه داده PostgreSQL را راه‌اندازی کنید
6. برنامه خود را مستقر کنید

## 🔮 نقشه راه آینده

- اپلیکیشن موبایل
- یکپارچه‌سازی درگاه پرداخت
- ویژگی‌های جلسه زنده
- تولید گواهینامه
- عناصر بازی‌سازی
- داشبورد تجزیه و تحلیل پیشرفته
- API برای یکپارچه‌سازی‌های شخص ثالث

</div> 