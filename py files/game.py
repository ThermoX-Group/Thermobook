import time
from timeit import default_timer as timer

start_time = timer()

first_num = int(input("yek adad az 1 ta 9 entekhab kon : "))
amaliat_aval=first_num*2
amaliat_dovom=amaliat_aval+8
amaliat_sevom=amaliat_dovom+first_num
amaliat_chaharom=amaliat_sevom-2
amaliat_panjom=amaliat_chaharom/3
amaliat_sheshom=first_num-amaliat_panjom
amaliat_haftom=amaliat_sheshom*4
print(amaliat_haftom+16)

end_time = timer()
print(f"[INFO] Total training time: {end_time-start_time:.3f} seconds")