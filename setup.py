from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
# -e là viết tắt của editable mode
# . nghĩa là thư mục hiện tại nơi chứa setup.py
# nếu không có -e . thì bạn chạy nó sẽ là pip install .
# nó sẽ copy toàn bộ file code bạn vào thư mục site-packages của Python
# là bạn sẽ có 1 bản gốc và 1 bản copy khi bạn thay đổi bản gốc thì bản copy sẽ không đổi
# còn nếu có -e thì bạn sẽ pip install -e .
# nó sẽ tạo ra 1 liên kết đến thư mục hiện tại và khi thay đổi thư mục gốc thì nó sẽ thay đổi bản còn lại
def get_requirements(file_path:str) -> List[str]: 
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="students_performance_mlproject",
    version="0.0.1",
    author="NhatNguyen",
    author_email="tnhatnguyen.dev2805@gmail.com",
    packages=find_packages(), # nó sẽ tìm các file __init__.py trong các thư mục con
    install_requires=get_requirements("requirements.txt"),
)
