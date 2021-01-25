
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<h1 style=\"text-align:center; color:black\"><b style=\"color:darkblue\">Python Basic</b> Session - 11</h1>|\n",
    "|:--:|\n",
    "| <img src=\"https://docs.google.com/uc?id=14xeXxFrVRjvOoUYWn_GuyE-v84wVzrqr\" class=\"img-fluid\" alt=\"CLRWY\" width=\"200\" height=\"100\"></h1>|\n",
    "\n",
    "> ## <font color=\"brown\">Loops </font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Give me a word : world\n",
      "w-o-r-l-d"
     ]
    }
   ],
   "source": [
    "word = input(\"Give me a word : \")\n",
    "count = 0\n",
    "\n",
    "for i in word :\n",
    "    count += 1\n",
    "    if count < len(word) :\n",
    "        i = i + \"-\"\n",
    "    print(i, end=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['world']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"world\".split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'world/jupiter/uranus'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"/\".join([\"world\", \"jupiter\", \"uranus\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "w-o-r-l-d\n"
     ]
    }
   ],
   "source": [
    "for i in word.split() :\n",
    "    print(\"-\".join(word))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_mix = [(\"one\", 1), (\"two\", 2), (\"three\", 3)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one 1\n",
      "two 2\n",
      "three 3\n"
     ]
    }
   ],
   "source": [
    "for string, integer in my_mix:\n",
    "    print(string, integer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('one', 1)\n",
      "('two', 2)\n",
      "('three', 3)\n"
     ]
    }
   ],
   "source": [
    "for i in my_mix:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "simple = {\"one\":1,\n",
    "          \"two\":2,\n",
    "          \"three\":3}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('one', 1), ('two', 2), ('three', 3)])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "simple.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one 1\n",
      "two 2\n",
      "three 3\n"
     ]
    }
   ],
   "source": [
    "for my_keys, my_values in simple.items() :\n",
    "    print(my_keys, my_values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(range(11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 11)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple(range(11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(range(11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 2 3 4 5 6 7 8 9 10 "
     ]
    }
   ],
   "source": [
    "for i in range(11):\n",
    "    print(i, end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 2 3 4 5 6 7 8 9 10\n"
     ]
    }
   ],
   "source": [
    "print(*range(11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"a\" < \"b\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "97"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ord(\"a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "98"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ord(\"b\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "text = ['one','two','three','four','five']\n",
    "numbers = [1, 2, 3, 4, 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<zip object at 0x000001835D25D688>\n"
     ]
    }
   ],
   "source": [
    "print(zip(text, numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(zip(text, numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('one', 1) ('two', 2) ('three', 3) ('four', 4) ('five', 5)\n"
     ]
    }
   ],
   "source": [
    "print(* zip(text, numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one : 1\n",
      "two : 2\n",
      "three : 3\n",
      "four : 4\n",
      "five : 5\n"
     ]
    }
   ],
   "source": [
    "for x, y in zip(text, numbers):\n",
    "    print(x, \":\", y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
