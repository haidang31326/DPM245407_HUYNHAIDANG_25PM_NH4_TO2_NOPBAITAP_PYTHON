import time
import os

def xoa_man_hinh():
    os.system('cls' if os.name == 'nt' else 'clear')


hinh_1 = """
       *
      * *
     * * *
    * * * * *
     * * *
    * * * *
    * *
"""


hinh_2 = """
       *
      * *
     * * *
    * * * * *
     * * *
    * *
    *
"""


hinh_3 = """
      * * *
     * * *
      * *
       *
      * *
     * * *
    * * * * *
"""


hinh_4 = """
    * * * * *
       * * *
        * *
         *
        * *
       * * *
    * * * * *
"""


cac_hinh_ve = [hinh_1, hinh_2, hinh_3, hinh_4]




for i, hinh in enumerate(cac_hinh_ve):
 
    xoa_man_hinh()
    

    print(f"--- Hình {i + 1} ---")
    
  
    print(hinh)
    
 
    print("\nChờ 5 giây để hiển thị hình tiếp theo...")
    time.sleep(5)


xoa_man_hinh()
print("Hoàn thành!")