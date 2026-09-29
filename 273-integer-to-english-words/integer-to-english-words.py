class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return 'Zero'

    belowTwenty = ['',        'One',       'Two',      'Three',
                   'Four',    'Five',      'Six',      'Seven',
                   'Eight',   'Nine',      'Ten',      'Eleven',
                   'Twelve',  'Thirteen',  'Fourteen', 'Fifteen',
                   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['',      'Ten',   'Twenty',  'Thirty', 'Forty',
            'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def helper(num: int) -> str:
      if num < 20:
        s = belowTwenty[num]
      elif num < 100:
        s = tens[num // 10] + ' ' + belowTwenty[num % 10]
      elif num < 1000:
      
