***HackerRank is a great base with different test tasks from interviews for data analysts. For this reason I decided to train my skills.***

**1. Plus Munis**
>
>Task:
>>Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
>>
>>Input Format
>>
>>>The first line contains an integer, n , the size of the array.
>>>
>>>The second line contains n space-separated integers that describe arr[n].
>>>
>>Output Format
>>
>>>Print the following  lines, each to  decimals:
>>>>
>>>>proportion of positive values
>>>>
>>>>proportion of negative values
>>>>
>>>>proportion of zeros
>>>>
>>>![image](https://github.com/user-attachments/assets/847bdbe9-45c2-4622-9f1f-4ffb5c815497)

>Solution:
>>       def plusMinus(arr):
         count_positive=0
         count_negative=0
         count_zero=0
         for i in arr:
          if i > 0:
            count_positive=count_positive+1
          elif i<0:
            count_negative=count_negative+1
          else:
            count_zero=count_zero+1
          total=count_positive+count_negative+count_zero
          proportion_positive=count_positive/total
          proportion_negative=count_negative/total
          proportion_zero=count_zero/total
          print(f'{proportion_positive:.5f}')
          print(f'{proportion_negative:.5f}')
          print(f'{proportion_zero:.5f}')

**2. Mini-Max Sum**
>
>Task:
>>Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
>>
>>Input Format
>>
>>>A single line of five space-separated integers.
>>>
>>Output Format
>>
>>>Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
>>>>
>>>![image](https://github.com/user-attachments/assets/ed337019-0f37-4143-aec3-d9049860370e)

>Solution:
>>     def miniMaxSum(arr):
         min=arr[0]
         max=arr[0]
         for i in arr:
             if i<min:
                  min=i
             if i>max:
                 max=i
         minsum = sum(arr)-max
         maxsum = sum(arr)-min  
         print(minsum,maxsum)   

