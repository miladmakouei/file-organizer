# File Organizer

A simple Python tool for organizing files by their extensions.

این پروژه برای تمرین کار با فایل‌ها و پوشه‌ها در پایتون ساخته شده است. برنامه فایل‌های یک پوشه را بررسی می‌کند و بر اساس پسوندشان، مقصد مناسب آن‌ها را مشخص می‌کند.

## Features | امکانات

- Organizes common file types into separate folders.
- Supports images, PDFs, documents, spreadsheets, text files, archives, audio, and videos.
- Shows a preview before moving files.
- Avoids overwriting files with the same name.
- Includes basic automated tests.

**توضیح:** برنامه ابتدا تغییرات پیشنهادی را نشان می‌دهد. فایل‌ها فقط زمانی جابه‌جا می‌شوند که گزینه `--apply` را اجرا کنیم.

## Requirements | پیش‌نیازها

- Python 3.10 or newer
- No external packages required

برای اجرای پروژه به نصب کتابخانه‌های جانبی نیاز نیست؛ ابزارهای موردنیاز در کتابخانه استاندارد پایتون وجود دارند.

## Project Structure | ساختار پروژه

```text
file-organizer/
├── organizer.py
├── test_organizer.py
├── README.md
└── .gitignore
```

- `organizer.py`: کد اصلی برنامه
- `test_organizer.py`: تست‌های خودکار
- `README.md`: راهنمای پروژه
- `.gitignore`: فایل‌هایی که نباید وارد Git شوند

## Usage | نحوه اجرا

### 1. Preview changes

ابتدا مسیر پوشه موردنظر را به برنامه بدهید تا فقط تغییرات پیشنهادی نمایش داده شوند:

```bash
python3 organizer.py ~/Downloads
```

در این حالت فایل‌ها جابه‌جا نمی‌شوند.

### 2. Organize files

پس از بررسی پیش‌نمایش، برای جابه‌جایی فایل‌ها دستور زیر را اجرا کنید:

```bash
python3 organizer.py ~/Downloads --apply
```

می‌توانید `~/Downloads` را با مسیر پوشه موردنظر خود جایگزین کنید.

**نکته:** بهتر است ابتدا برنامه را روی یک پوشه آزمایشی اجرا کنید. جابه‌جایی فایل‌ها با گزینه `--apply` انجام می‌شود و برنامه قابلیت بازگردانی خودکار ندارد.

## Run Tests | اجرای تست‌ها

برای بررسی عملکرد برنامه، از مسیر اصلی پروژه دستور زیر را اجرا کنید:

```bash
python3 -m unittest -v
```

تست‌ها از پوشه‌های موقت استفاده می‌کنند و برای اجرا نیازی به فایل‌های شخصی شما ندارند.

## How It Works | نحوه عملکرد

1. مسیر پوشه بررسی می‌شود.
2. پسوند فایل‌ها خوانده می‌شود.
3. برای هر فایل پشتیبانی‌شده، پوشه مقصد مشخص می‌شود.
4. در حالت پیش‌نمایش، فقط عملیات پیشنهادی نمایش داده می‌شود.
5. در حالت اجرا، پوشه‌های لازم ساخته می‌شوند و فایل‌ها جابه‌جا می‌شوند.
6. اگر فایل هم‌نامی در مقصد وجود داشته باشد، نام جدیدی برای فایل انتخاب می‌شود.

## Limitations | محدودیت‌ها

- فقط فایل‌های داخل همان پوشه بررسی می‌شوند؛ زیرپوشه‌ها به‌صورت بازگشتی بررسی نمی‌شوند.
- دسته‌بندی بر اساس پسوند فایل انجام می‌شود.
- فایل‌هایی با پسوندهای پشتیبانی‌نشده بدون تغییر باقی می‌مانند.
- قابلیت بازگردانی خودکار عملیات وجود ندارد.

## What I Learned | چیزهایی که تمرین کردم

در این پروژه با موارد زیر کار کردم:

- Python functions and dictionaries
- `pathlib` for working with file paths
- `argparse` for command-line arguments
- `shutil` for moving files
- Error handling
- Unit testing with `unittest`

هدف این پروژه تمرین کار با فایل‌ها، نوشتن توابع قابل‌استفاده مجدد و بررسی عملکرد برنامه با تست‌های خودکار است.

## License

This project is for learning and portfolio purposes.