import os
from zipfile import ZipFile


def zip_individual_files_and_folder(directory, output_folder):
    """
    ضغط ملفات ومحتويات مجلدات بشكل فردي.

    Args:
        directory (str): المسار إلى المجلد الذي يحتوي على الملفات والمجلدات.
        output_folder (str): المسار الذي سيتم فيه حفظ الملفات المضغوطة.
    """
    # يمر عبر جميع العناصر داخل المجلد المعطى
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # إذا كان الملف، ضغطه بملف ZIP فردي
        if os.path.isfile(item_path):
            output_path = os.path.join(output_folder, f"{item}.zip")
            with ZipFile(output_path, "w") as zipf:
                zipf.write(item_path, os.path.basename(item_path))
            # قم بفعل ذلك إذا كنت ترغب في حذف الملف الأصلي بعد الضغط
            # os.remove(item_path)
            print(f"{item} تم ضغطه بنجاح وتم حذف الملف الأصلي")
        # إذا كان مجلد، ضغط محتوياته في ملف ZIP واحد
        elif os.path.isdir(item_path):
            base_name = os.path.basename(item_path)
            output_path = os.path.join(output_folder, f"{base_name}_contents.zip")
            with ZipFile(output_path, "w") as zipf:
                # قم بفحص جميع الملفات داخل المجلد وقم بضغطها
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, item_path)
                        zipf.write(file_path, arcname)
            print(f"{base_name} تم ضغط محتوياته بنجاح في ملف {base_name}_contents.zip")


if __name__ == "__main__":
    # حدد المسار الذي يحتوي على الملفات والمجلد
    input_directory_path = rf"/path/to/your/input/folder"
    # حدد المسار الذي تريد فيه حفظ الملفات المضغوطة
    output_directory_path = rf"/path/to/your/output/folder"
    # قم بتشغيل السكربت
    zip_individual_files_and_folder(input_directory_path, output_directory_path)
