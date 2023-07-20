import base64
from tkinter import *

icon = "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAACAASURBVHic7d15sG1nWefx70MGMhAyCDEDCjYBaURCZBDBCFakLcNwE4UmahnEpmiqKRBQQMJgMQk0oBG1WkUQsFUiQnKD4ABIIGooDCQoxBCgW4QMTQxCAgm5Se7Tf6wVQkLuzcm9e+9nn/f5fqp23bp/nd9ba53n/e2111k7MhPVi4g7A/cADgeOmF+H3+Lfw4C9iyJK0m3ZBlwGXApcMr8uvcW//5qZV5Yl1DeFBaBORNwd2AKcABwL7FmbSJKW7nrgbOAMYGtmfr44T1sWgBWLiAdw06b/gOI4klTtfG4qA+dXh+nEArAC8zv9ZwEnAncvjiNJ6+rzwOnAqV4ZWD4LwBJFxCHAC4GnA3csjiNJm8W1wO8Ar8zML1eHGZUFYAkiYl/gmcCvAAcVx5GkzeorwKuBN2TmNdVhRmMBWKCIuAPwJOBlwN2K40jSKL4IvAR4a2Zurw4zCgvAgkTEccCpwP2qs0jSoD4JPCszP1AdZAR3qA4wgoh4LvA3uPlL0jLdD/ibeeZqN3kFYDdExB2B3wdOrs4iSc28DXhqZl5bHWSzsgDsoog4jOnPVR5anUWSmvoIcGJmXlYdZDOyAOyCiPgBYCve6CdJ1b4IbMnMj1cH2Wy8B+B2iognMD3G0s1fkurdDTh7ns26HSwAt0NEPBk4DdivOosk6Zv2A06bZ7Q2yI8ANigifhj4AH4bnyStq23AcZn5d9VBNgMLwAbMz/L/KHBodRZJ0k59CXiI3yVw2/wI4DZExP5MN/y5+UvS+jsU2DrPbu2EBWAnIiKAPwKOrs4iSdqwo4E/mme4dsACsHMvY/oKX0nS5nIi0wzXDngPwA5ExBOBt1fnkCTtlpMy87TqEOvIAnArIuJA4HPAd1RnkSTtliuAe2bmV6uDrBs/Arh1z8fNX5JG8B1MM1234BWAW4iII4HPAPtWZ5EkLcQ1wFGZeUl1kHXiFYBv91Lc/CVpJPviDYHfxisA3yIi7gv8E7BHdRZJ0kLdANw/My+oDrIuvAJwc6/GzV+SRrQH04zXzCsAs4g4FvhwdQ5J0lL9SGaeXR1iHXgF4CYvrw4gSVo6Z/3MKwBARBwOXAz42EhJGlsCR2bmpdVBqnkFYPI43PwlqYNgmvntWQAmW6oDSJJWxpmPHwEQEQcA/w7sXZ1FkrQS24C7ZOZV1UEqeQUAfgI3f0nqZG+m2d+aBcBLQZLUUfvZ3/ojgIjYC7gcOLA6iyRppb4K3DUzr6sOUqX7FYBH4uYvSR0dyLQHtNW9ABxTHUCSVKb1HtC9ABxeHUCSVOaI6gCVuheA1gdfkppr/SbQAiBJ6qr1HtC9ALRuf5LUXOs9oPufAV4N7FudQ5JU4prM3K86RJW2VwAi4kDc/CWps30j4qDqEFXaFgCaf/YjSQIafwxgAZAkddZ2L+hcAA6oDiBJKtd2L+hcACRJassCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNbRndQCtnRuATwH/CJwLfKU2jqQFujPwIODBwP1wD2jNg68b/Q3wcuDjmXl1dRhJS/P7ABGxL3AM8ELg+NJEKuFHALoSeGpm/nhm/p2bv9RDZl6Tmf+QmY8G/hvTLFAjFoDe3g98f2a+sTqIpDqZ+WamjwTeX51Fq2MB6OsC4DGZ+W/VQSTVy8wvAI9hmg1qwALQ0/XAkzLz2uogktbHPBOexDQjNDgLQE+vycxzq0NIWj/zbHhNdQ4tnwWgnwuBl1WHkLTWXsY0KzQwC0A/f5mZ26pDSFpf84x4T3UOLZcFoB8v/UvaiH+sDqDlsgD087HqAJI2BQvA4CwAvVwJXFQdQtL6y8z/A1xRnUPLYwHo5aLMzOoQkjaNf6kOoOWxAPRyQ3UASZuKM2NgFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAejlrtUBJG0qzoyBWQB6+U8RcXB1CEnrLyIOAO5TnUPLYwHo54HVASRtCg/EPWJoHtx+LACSNuLB1QG0XBaAfn6wOoCkTeGHqgNouSwA/WyJiIdXh5C0vuYZsaU6h5bLAtDPHYA/jIj9qoNIWj/zbPhD3B+G5wHu6V7Aq6pDSFpLr2KaERqcBaCvZ0TET1aHkLQ+5pnwjOocWg0LQF8BvDMi3hQRd64OI6lORBwQEW8E3sk0G9SABUC/AHwyIn6sOoik1YuIHwX+GXhKdRat1p7VAbQWvgt4X0T8A3Du/PoYcGFmbi9NJmlhIuIOwL2ZngfyoPn1cHzX35IFQN/qYfPrRldHxFVVYSQt3J2A/atDaD1YALQz+80vSdJgvAdAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDe1YH0Fq4BngfcCZwIXAxcGlmXrvKEBFxCHAEcCRwLLAFuN8qM2wC24G/B84AzmM6Vpdk5tdWGSIi7sRNx+oY4ATg4fim4pY+CWwFzuamY/XlVQaIiDsChzMdq/sAjwMeBey7yhxaP5GZ1RlKRMQJwOnVOYpdBrwUeFtmXl0d5tZExPcCLwF+GojiOJWuAU4FfiMzL68Oc2si4q7As4Fn0XtzSeBPgZdl5qerw9yaiNgPOBn4VeCw4jjVTszMM6pDVLCt97QdeAVwVGb+7rpu/gCZ+enM/FngQcC51XmK/Blwr8w8ZV03f4DMvDwzTwHuxZS5o3OBB2Xmz67r5g+QmVdn5u8CRzHNgu3FkVTAAtDPVcCWzHxxZn69OsxGZebHmT4W+NPqLCuUwAsy84mZeXF1mI3KzIsz84nAC5jW0MWfAsfO5+qmkJlfz8wXM33cdlV1Hq2WBaCX/wAenpl/UR1kV2TmNzLzZ4DXVWdZge3ASZn56uogu2rOfhI93l2+LjN/JjO/UR1kV8wz4eFMM0JNWAD6uB54Qmb+c3WQBXge8K7qEEt2SmZu+svo8xpOqc6xZO9iOic3tXk2PIFpVqgBC0Afv5yZH6gOsQg53bl6MvCp6ixL8vbMfE11iEWZ1/L26hxL8ing5Bzkbup5RvxydQ6thgWgh08Bv1UdYpHm+xd+qTrHElwNPKc6xBI8h2lto/mlzXQvzQb9FuOWa30LC0APp2TmcJ/DZuZfAx+szrFgv5mZl1aHWLR5Tb9ZnWPBPjifg0OZZ8XoH9sIC0AHF2bmmdUhluh/VgdYoBuA11eHWKLXM61xFCOdezczz4wLq3NouSwA4xv9ARd/C1xZHWJBzs7MK6pDLMu8trOrcyzIlUzn3shGnx3tWQDGN/QvcWZuA95bnWNBhj5Ws1HW+N753BvZKMdKO2ABGNt24GPVIVbgH6sDLMgo69iZUdY4yjp25mP0eIZDWxaAsX0pMzv8Te+meUrebbikOsAKjLLGUc65HZpnx9o+elq7zwIwtlGG7W0ZYZ3JGOu4LZcwxuOBOxwraFB0OrMAjK3Ls71HWOe2Bp8p33jPxgjrHOGc24gu62zJAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBWBse1YHWJER1rlHRER1iGWb17hHdY4FGOGc24gu62zJAjC2w6sDrMgI69wTuEt1iBW4C2NsKiOccxvRZZ0tWQDGdkR1gBUZZZ2jrGNnRlnjKOu4LV3W2ZIFYGz7RMSR1SFW4KjqAAsyyjp2ZpQ1jrKOHZpnxz7VObQ8FoDxPaY6wAqMssZR1rEzo6xxlHXsTIc1tmYBGN+W6gDLFBH3Bu5TnWNBHhMRI9wgd6vmtY2yqdxnPvdGNvTskAWgg+Mi4rurQyzRL1QHWKC7AI+tDrFEj2WsGx1HOvduZp4Zx1Xn0HJZAMa3N/DS6hDLEBFHAM+ozrFgr4yI4X4v5zW9sjrHgj1jPgdH9FKm2aGBDTdodKtOjojvrw6xBC8F9qsOsWD3BZ5cHWIJnsy0tpHsx4Dlep4VJ1fn0PJZAHq4A/COiDioOsiiRMRPA0+pzrEkp45U2Oa1nFqdY0meMp+LQ5hnxDtwb2jBg9zH9wKnjXCTWUQ8BHhzdY4luhNwZkTctTrI7prXcCbTmkb15vmc3NTm2XAa06xQAxaAXv4LsDUiDqgOsqsi4jjgrxj/75PvAXwoIu5ZHWRXzdk/xLSWke0D/NV8bm5K80zYyjQj1IQFoJ9HA+dsxo0lIp7OtPkfXJ1lRf4z8NHNuLHMmT/KtIYODmYqAU+vDnJ7zbPgHKbZoEYsAD19H/CpiHhtRKz9ZhoRx0bEOcBvM8Zz5G+PQ4D3R8RpEbH2T5+LiKMi4jTg/UzZO9kT+O2IOCcijq0Oc1si4uCIeC3wKaaZoGYiM6szlIiIE4DTq3Osga8wfe63FfhAZm4rzgNARHwX8Djg8cAja9OsjeuAM+bXezPzK8V5gG/eOHY8cML82qs20do4C/hz4MzM/EJxFgAiYm+mv+/fAjwRGObG4N1wYmaeUR2iggVA3+rrwP8FLgYuBa5d8c8/hOnLR45k/M+Nd9d13HSsLgG+tuKffyduOlbfg5v+bflXbjpWXwZWOXj3YfpWvxuP1f4r/NmbwQmZubU6RIVul1O1c/sD95tfWm97AfeeX1p/98BSu66iOkAV7wGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDe1YH0Fq5FvgCcDFw6fz/VToEOAI4EjhsxT97s9kOfJHpWF0CfG3FP/9O3HSs7oZvJm7LZdx0rL4M5Ap/9j7A4UzH6ruAO67wZ28GqzwWa8UCoKuAdwFbgb/OzKuL8wAQEUcBW4DHAw8tjrMubgDeC5wBvDszLy/OA0BE3BV4LHACcDywR22itfER4M+BrZn52eowABGxH/DjTL9bPwkcUJtoLUR1gCqR2bP8RMQJwOnVOQpdB/we8LJ12Uh2JCIeBbwGOKY6S6EzgRdk5gXVQXYmIu4LvAp4XHWWQucBz8/M91UH2Zm5uL0E+O/AXsVxKp2YmWdUh6jgZbueLgKOzsxnrPvmDzAP0gcCv8x06buTrwKPzswt6775A2TmBZm5BXg0U/ZOtjOdow9c980fIDMvz8xnAEczzQQ1YwHo533AD2bmv1QHuT1y8nqmS81XVudZkc8CD83M91YHub3mzA9lWkMHVwKPzczX5ya7rDrPgh9kmg1qxALQy1lM7ya/Uh1kV80by/HAtuosS/ZF4NjMvLA6yK6asx/LtJaRbQOO34xF7UbzTHg004xQExaAPj4HPD4zr6sOsrsy8++Bp1bnWKKrgS2ZeVl1kN01r2EL05pG9dT5nNzU5tnweKZZoQYsAD1sB56QmVdUB1mUzHwr8JbqHEvynMz8eHWIRZnX8pzqHEvylvlcHMI8I55Av3ttWrIA9PDHmXledYgleBFwTXWIBfsX4A+qQyzBHzCtbSTXMJ2DQ5lnxR9X59DyWQDGt40BhxRAZl4MvKE6x4Kdkpk3VIdYtHlNp1TnWLA3zOfgiF7E+PfZtGcBGN/fZua/VYdYoj+sDrBAVwDvrg6xRO9mWuMoRjr3bmaeGX9bnUPLZQEY39bqAMuUmZ8GPl2dY0H+YsR3/zea1/YX1TkW5NPzuTeyoWeHLAAdvKc6wAqMssZR1rEzo6xxlHXsTIc1tmYBGNs3MvML1SFW4DPVARZklHXszChrHGUdOzTPjm9U59DyWADGdkl1gBUZ5UasDsdrlDWOcs7dlkurA2h5LABj2/QPktmgEdZ5PbD238uwAJczrXWzG+Gc2wgLwMAsAGPb9E/926AR1nnDZnuG/K6Y1zjCjY4jnHMb0WWdLVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIAjO1O1QFWZIR17h0Re1WHWLZ5jXtX51iAEc65jeiyzpYsAGM7sjrAioywzgCOqA6xAkcwrXWzG+Gc24gu62zJAjC2QyNiz+oQKzDKxjnKOnZmlDWOso4dmmfHodU5tDwWgLHdATimOsQKPKg6wIKMso6dGWWNo6xjZ47BPWJoHtzxbakOsEzzZ8rHV+dYkKGP1WyUNR7f4J6NUY6VdsACML4TqwMs2SOBg6pDLMgjIuLg6hDLMq/tEdU5FuQgpnNvZKPPjvYsAOO7b0SM8g751jy3OsAC7Qk8uzrEEj2baY2jGOncu5l5Zty3OoeWywLQw6siYrhjHRHHAY+qzrFgz4mI76wOsWjzmp5TnWPBHjWfg0OZZ8WrqnNo+YbbFHSr7g88rTrEIkXEvsCvV+dYgv2B11aHWILXMq1tNL8+n4sjeRrTzNDgLAB9nBoRP1IdYoHezLhD6uci4lnVIRZlXsvPVedYkvsznYtDmGfEqdU5tBoWgD72At4ZEfepDrK7IuLlwEnVOZbsdRGx6e/CntfwuuocS3bSfE5uavNseCfTrFADFoBe7gKcExGb8nPziNg7It4MvKg6ywrswVTYNu2VgDn7O5nWMroXRcSbI2JTPuZ4ngnnMM0INWEB6Ocg4C8j4oURsU91mI2KiO8DPgg8uTrLCu0B/EZEvDUiNs0T2SLi0Ih4K/Ab9Nj8b/Rk4IPzubopRMQ+EfFC4C8Z589ptUEWgJ72AF4BXBQRP7/O71oi4h4R8SbgE8DDqvMUORn4XES8JCLWdkhHxEER8RLgc0yZO3oY8ImIeFNE3KM4yw7NV9N+HriIaRZ0KmqaRWZWZygREScAp1fnWBNXMb0DOBO4ELgY+FJmbl9liIjYj+kZ60cCxzI9iazDI1dvj+uAs4AzgPOYjtWlmXndKkPMT8E7nOlYHQOcwPRgHD8/vrlzga3A2UzH6pLMvHqVAeY/6zuU6VjdB3gc8BPAAavMscZOzMwzqkNUsABoR24Arl/xz7zjin/eKBLYtuKfuTdjfKtfhWtX/PP2xHf4O9O2AIz0VC4t1h44NDaLwPK0mXistBa8B0CSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ3tWR1Aa+PLwHuBC4GLgUuBa1ec4RDgCOBI4Fjgh7Ck3ppvAO8DzmM6VpcAXytNpHV2R+Bwpt+r+wDHM/2uaZLVAapYAHpL4M+A3wXOzswbivPcTEQcCpwIPB/4nuI46+Ac4HXAX2fm16vDaHOKiD2YCvbTgP8KRG2icm3X77urvj4MPCQzT8rMs9Zt8wfIzC9l5u8xvWt5NvCV4khVPgv8ZGY+LDPf5eav3ZGZN8y/8ycBD2GaBWrIAtDTa4Efzcxzq4NsRGZuy8xTgQczfUTRyXuBB2bm6dVBNJ55Bvwo00xQMxaAXrYDT87M52Xm9uowt1dmfhZ4KPDB6iwr8lvAYzPzyuogGldmbs/M5wFPZpoRasIC0MvzM/Mt1SF2R2Z+FTgBuKA6y5L9OfCLm7GoaXOaZ8Pzq3NodSwAfbw1M19XHWIR5nfEj2P6y4URnQc8KTPb3p2sGvOMeGt1Dq2GBaCHy4FnVodYpMz8HPCi6hxLkMBTMvPq6iBq65lMM0ODswD08IpBP0d+I3BRdYgFe3tmfrw6hPqaZ8UrqnNo+SwA47sM+F/VIZYhM69nvEH1q9UBJKaZcVl1CC2XBWB8WzPzuuoQS7QV2FYdYkE+kZmfqQ4hzTNja3UOLZcFYHxD/xLPlyvPqs6xIEMfK206no+DswCM70PVAVbgrOoAC3JWdQDpW3SYHa1ZAMb2H03uJr+4OsCCjLIODWCeHf9RnUPLYwEYW5cNZZR1jrIOjcNzcmAWgLFdUR1gRUZY57V+yY/W0Ai/W9oBC4AkSQ1ZACRJasgCIElSQxYASZIasgBIktSQBUCSpIYsAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFoCxRXWAFRlhnSOsQePxvByYBWBsh1YHWJER1rl3RBxYHUK6hRF+t7QDFoCxHVEdYEVGWeco69A4PCcHZgEY252bvKv87uoACzLKOjSAeXbcuTqHlscCML4fqw6wAqOscZR1aAyej4OzAIxvS3WAZYqIuwIPq86xIEMfK206no+DswCM7zERsX91iCV6AuOcx/eKiB+oDiHNM+Mx1Tm0XKMMTu3YwcBzqkMsQ0TsC5xSnWPBXl4dQGKaGQdXh9ByWQB6eG5E3KU6xBI8EziyOsSCHR8Rj6gOob7mWfHc6hxaPgtADwcAb4qIYY53RBwNvLg6x5K8MSJ896WVm2fEm5hmhgY3zIag2/Q44NeqQyxCRBwKnAmMem/DvYB3RMSe1UHUzq8xzQo1YAHo5fkR8YLqELsjIo4E/orx/2b+OOB/R8Q+1UHUwzwbnl+dQ6tjAejn1yLiT+Yb6DaViHgocC5wTHWWFXkicPZceqSliIh9I+JPGOQKoTbOAtDTTwPnR8QJ1UE2IiIOjohfBz4EHFadZ8UeBPxTRPxiROxVHUZjmWfA+UwzQc1YAPq6N3B6RHwoIk5ax0cGR8T3RcSvAp8Dng3sXRypyiHAqcAFEfE/vCKg3RERB86/8x8CTmeaBWooMrM6Q4m5+Z5enWONXMf0Dvsi4DLg/wHbVpzhIKZ3+IcBPwzcc8U/f7NIpo9CzuemY/X10kRaZ3sD38n0e3Vv4BGAV5NuckJmbq0OUcG7jHWjvZie/e3zv9dfAA+eX5J2T1QHqOJHAJIkNWQBkCSpIQuAJEkNWQAkSWrIAiBJUkMWAEmSGrIASJLUkAVAkqSGLACSJDVkAZAkqSELgCRJDVkAJElqyAIgSVJDFgBJkhqyAEiS1JAFQJKkhiwAkiQ1ZAGQJKkhC4AkSQ1ZACRJaqhzAbiqOoAkqVzbvaBzAbikOoAkqVzbvcACIEnq7NLqAFUiM6szlImIq4F9q3NIkkpck5n7VYeo0vkKAHgVQJI6a70HdC8AbS/9SJJ67wHdC0Dr9idJzbXeAywAkqSuvALQWOuDL0nNtX4T2L0AnFcdQJJUpvUe0P3PAPcCLgcOrM4iSVqprwJ3zczrqoNUaX0FYD7w76nOIUlaufd03vyheQGYba0OIElaufazv/VHAAARcQDw78De1VkkSSuxDbhLZrb9IiDwCgDzCfCB6hySpJX5QPfNHywAN2p/KUiSGnHm40cAAETE4cDFQFRnkSQtVQJHZmb758B4BQCYT4QPV+eQJC3dh938JxaAm7y4OoAkaemc9TMLwCwzzwbeXZ1DkrQ0755nvfAegJuJiPsC/wTsUZ1FkrRQNwD3z8wLqoOsC68AfIv5xHhLdQ5J0sK9xc3/5rwCcAsRcSTwGWDf6iySpIW4BjgqM1t/+98teQXgFjLzYuDU6hySpIU51c3/23kF4FZExIHA54DvqM4iSdotVwD3zMyvVgdZN14BuBXzifL06hySpN32dDf/W2cB2IHMPA14RXUOSdIue8U8y3Ur/AhgJyIigHcCJ1ZnkSTdLqcDP5VucjtkAbgNEbE/8PfA0dVZJEkb8gng4Zn59eog68wCsAERcXfgUkrM6wAAAbpJREFUo8Ch1VkkSTv1JeAhmfn56iDrznsANmA+kX4K2FadRZK0Q9uYLvu7+W+ABWCDMvPvgKcxfZWkJGm9JPC0eVZrA/wI4HaKiCcwPS54v+IokqTJ1cDPZ+Y7qoNsJhaAXRARPwBsBe5WnUWSmvsisCUzP14dZLPxI4BdMJ9oDwY+Up1Fkhr7CPBgN/9dYwHYRZl5GfBI4G3FUSSpo7cBj5xnsXaBBWA3ZOa1mfkk4HnA9uo8ktTAduB5mfmkzLy2Osxm5j0ACxIRxzF9i+D9qrNI0qA+CTwrMz9QHWQEXgFYkPmEPBr4BaabUiRJi/FFptl6tJv/4ngFYAkiYl/gmcCvAAcVx5GkzeorwKuBN2TmNdVhRmMBWKKIOAR4IdNXC9+xOI4kbRbXAr8DvDIzv1wdZlQWgBWYv0vgWUzfKnj34jiStK4+z/Qtfqf6ON/lswCsWEQ8ANgCnAA8oDiOJFU7HzgD2JqZ51eH6cQCUGi+MnBjGTgW2LM2kSQt3fXA2dy06ftOv4gFYE1ExJ2BewCHA0fMr8Nv8e9hwN5FESXptmwDLgMuBS6ZX5fe4t9/zcwryxLqm/4/Th5/HvZ4BBkAAAAASUVORK5CYII="

root = Tk()
root.title("Calculator")
root.iconphoto(True, PhotoImage(data=icon))
root.config(bg="black")
root.geometry("320x394") #
root.resizable(False,False)
equation = ""

def show(value):
    global equation
    equation+=value
    entry.config(text=equation)
def clear():
    global equation
    equation = ""
    entry.config(text=equation)
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error!"
    entry.config(text=result)

entry = Label(root,text="",width=15,height=3,font="arial 20")
entry.grid(row=0,column=0,columnspan=4,sticky="nsew")

but_1 = Button(root,text="1",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("1"))
but_2 = Button(root,text="2",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("2"))
but_3 = Button(root,text="3",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("3"))
but_4 = Button(root,text="4",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("4"))
but_5 = Button(root,text="5",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("5"))
but_6 = Button(root,text="6",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("6"))
but_7 = Button(root,text="7",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("7"))
but_8 = Button(root,text="8",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("8"))
but_9 = Button(root,text="9",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("9"))
but_0 = Button(root,text="0",padx=72,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("0"))

but_clear = Button(root,text="C",font=("arial",10,"bold"),bd=1,padx=30,pady=15,bg="#3697f5",command=clear)
but_add = Button(root,text="+",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("+"))
but_minus = Button(root,text="-",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("-"))
but_divide = Button(root,text="÷",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("/"))
but_modu = Button(root,text="%",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("%"))
but_multi = Button(root,text="×",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("*"))
but_dot = Button(root,text=".",width=10,height=3,fg="white",bg="#2a2d36",bd=1,command=lambda:show("."))
but_equal = Button(root,text="=",width=10,pady=45,fg="black",bg="#fe9037",bd=1,command=calculate)

but_multi.grid(row=1,column=0,padx=1,pady=2)
but_modu.grid(row=1,column=1,padx=1,pady=2)
but_divide.grid(row=1,column=2,padx=1,pady=2)
but_clear.grid(row=1,column=3,padx=2,pady=2)

but_1.grid(row=2,column=0,pady=2)
but_2.grid(row=2,column=1,pady=2)
but_3.grid(row=2,column=2,pady=2)
but_minus.grid(row=2,column=3,pady=2)

but_4.grid(row=3,column=0,pady=2)
but_5.grid(row=3,column=1,pady=2)
but_6.grid(row=3,column=2,pady=2)
but_add.grid(row=3,column=3,pady=2)

but_7.grid(row=4,column=0,pady=2)
but_8.grid(row=4,column=1,pady=2)
but_9.grid(row=4,column=2,pady=2)
but_equal.grid(row=4,column=3,rowspan=2,pady=2)

but_0.grid(row=5,column=0,columnspan=2,pady=2)
but_dot.grid(row=5,column=2,pady=2)

#Centralize Window
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()
