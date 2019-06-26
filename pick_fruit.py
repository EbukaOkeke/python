{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 347,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import random\n",
    "fruit_basket = {'apple': 8, 'banana': 2, 'orange': 1}\n",
    "\n",
    "def pick_fruit(fruit_basket):\n",
    "    sum_of_values = sum(fruit_basket.values())\n",
    "    fruit_basket_prob = {k: v/float(sum_of_values) for k, v in fruit_basket.items()}\n",
    "    print(fruit_basket_prob)\n",
    "    return np.random.choice(list(fruit_basket_prob.keys()), 10, p=list(d2.values()))\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'apple': 0.7272727272727273, 'banana': 0.18181818181818182, 'orange': 0.09090909090909091}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array(['apple', 'apple', 'banana', 'apple', 'orange', 'orange', 'orange',\n",
       "       'apple', 'orange', 'apple'], dtype='<U6')"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print(sum_of_values)\n",
    "pick_fruit(fruit_basket)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
