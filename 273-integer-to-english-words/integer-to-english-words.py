class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return 'Zero'

    belowTwenty = ['',        'One',       'Two',      'Three',
                   'Four',    'Five',      'Six',      'Seven',
                   'Eight',   'Nine',      'Ten',      'Eleven',
                   'Twelve',  'Thirteen',  'Fourteen', 'Fifteen',
    
