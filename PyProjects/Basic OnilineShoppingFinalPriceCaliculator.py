fp=int(input())
fd=int(input())
fsp=int(input())
sp=int(input())
sd=int(input())
ssp=int(input())
ap=int(input())
ad=int(input())
asp=int(input())
if (0>fp or fp>10**9 or 0>fd or fd>100 or 0>fsp or fsp>10**9 or
    0>sp or sp>10**9 or 0>sd or sd >100 or 0>ssp or ssp>10**9 or
    0>ap or ap>10**9 or 0>ad or ad>100 or 0>asp or asp>10**9):
    print("Invalid")
else:
      discountf=(fd/100)*fp
      flipkartfinalprice=fp-discountf+fsp
      print("In Flipkart: Rs.",int(flipkartfinalprice),sep=(''))
      discounts=(sd/100)*sp
      snapdealfinalprice=sp-discounts+ssp
      print("In Snapdeal: Rs.",int(snapdealfinalprice),sep=(''))
      discounta=(ad/100)*ap
      amazonfinalprice=ap-discounta+asp
      print("In Amazon: Rs.",int(amazonfinalprice),sep=(''))
      if (flipkartfinalprice <= snapdealfinalprice) and (flipkartfinalprice <= amazonfinalprice):
        print("He will prefer Flipkart")
      elif (snapdealfinalprice <= flipkartfinalprice) and (snapdealfinalprice <= amazonfinalprice):
        print("He will prefer Snapdeal")
      else:
        print("He will prefer Amazon")