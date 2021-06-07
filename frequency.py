# Python code to demonstrate each occurrence frequency
  
# initializing string 
test_str = "//Hope is the essence of life. Many of us could not even live a life of peace without having hope deep inside the heart. Life is unpredictable, hard and quite notorious at times. Things go out of hand and beyond of our control many times. Hope helps us keep the fight on and improves the chances of making our life better. Hope – the essence of life keeps our eyes wide open for an improved future. I know it’s very hard keeping up with the inner faith during the most critical times, but, those who never leave hope, actually make it till the end."
  
# get count of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ("Count of all characters in given para is :\n "
                                        +  str(all_freq))