{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1.0\n",
       "1    3.0\n",
       "2    5.0\n",
       "3    NaN\n",
       "4    6.0\n",
       "5    8.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Series\n",
    "s = pd.Series([1, 3, 5, np.nan, 6, 8])\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-01-01</th>\n",
       "      <td>-1.016938</td>\n",
       "      <td>2.024969</td>\n",
       "      <td>-0.059282</td>\n",
       "      <td>0.842647</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-02</th>\n",
       "      <td>-1.018664</td>\n",
       "      <td>-1.006544</td>\n",
       "      <td>0.451620</td>\n",
       "      <td>-0.592781</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-03</th>\n",
       "      <td>-0.402324</td>\n",
       "      <td>-0.842240</td>\n",
       "      <td>2.158730</td>\n",
       "      <td>-0.767963</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-04</th>\n",
       "      <td>0.003951</td>\n",
       "      <td>1.596461</td>\n",
       "      <td>0.158366</td>\n",
       "      <td>0.528652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-05</th>\n",
       "      <td>-0.151427</td>\n",
       "      <td>1.707160</td>\n",
       "      <td>-0.976849</td>\n",
       "      <td>-0.294236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-06</th>\n",
       "      <td>-1.045103</td>\n",
       "      <td>-0.116764</td>\n",
       "      <td>-0.571053</td>\n",
       "      <td>-0.476454</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2013-01-01 -1.016938  2.024969 -0.059282  0.842647\n",
       "2013-01-02 -1.018664 -1.006544  0.451620 -0.592781\n",
       "2013-01-03 -0.402324 -0.842240  2.158730 -0.767963\n",
       "2013-01-04  0.003951  1.596461  0.158366  0.528652\n",
       "2013-01-05 -0.151427  1.707160 -0.976849 -0.294236\n",
       "2013-01-06 -1.045103 -0.116764 -0.571053 -0.476454"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define df we will use it for the rest of the tutorial\n",
    "dates = pd.date_range(\"20130101\", periods=6)\n",
    "df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list(\"ABCD\"))\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "      <th>F</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>test</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>train</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>test</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>train</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>validate</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A          B    C  D         E    F\n",
       "0  1.0 2013-01-02  1.0  3      test  foo\n",
       "1  1.0 2013-01-02  1.0  3     train  foo\n",
       "2  1.0 2013-01-02  1.0  3      test  foo\n",
       "3  1.0 2013-01-02  1.0  3     train  foo\n",
       "4  1.0 2013-01-02  1.0  3  validate  foo"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = pd.DataFrame({\n",
    "    \"A\": 1.0,\n",
    "    \"B\": pd.Timestamp(\"20130102\"),\n",
    "    \"C\": pd.Series(1, index=list(range(5)), dtype=\"float32\"),\n",
    "    \"D\": np.array([3]*5, dtype=\"int32\"),\n",
    "    \"E\": pd.Categorical([\"test\", \"train\", \"test\", \"train\", \"validate\"]),\n",
    "    \"F\": \"foo\"\n",
    "})\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "      <th>F</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>train</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>validate</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A          B    C  D         E    F\n",
       "3  1.0 2013-01-02  1.0  3     train  foo\n",
       "4  1.0 2013-01-02  1.0  3  validate  foo"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.tail(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "      <th>F</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>test</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A          B    C  D     E    F\n",
       "0  1.0 2013-01-02  1.0  3  test  foo"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1.0\n",
       "1    1.0\n",
       "2    1.0\n",
       "3    1.0\n",
       "4    1.0\n",
       "Name: C, dtype: float32"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[\"C\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "      <th>F</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>test</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2013-01-02</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>train</td>\n",
       "      <td>foo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A          B    C  D      E    F\n",
       "0  1.0 2013-01-02  1.0  3   test  foo\n",
       "1  1.0 2013-01-02  1.0  3  train  foo"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Select a row\n",
    "df2[0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A   -1.016938\n",
       "B    2.024969\n",
       "C   -0.059282\n",
       "D    0.842647\n",
       "Name: 2013-01-01 00:00:00, dtype: float64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selection by Label\n",
    "df.loc[dates[0]]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-01-01</th>\n",
       "      <td>-1.016938</td>\n",
       "      <td>2.024969</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-02</th>\n",
       "      <td>-1.018664</td>\n",
       "      <td>-1.006544</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-03</th>\n",
       "      <td>-0.402324</td>\n",
       "      <td>-0.842240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-04</th>\n",
       "      <td>0.003951</td>\n",
       "      <td>1.596461</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-05</th>\n",
       "      <td>-0.151427</td>\n",
       "      <td>1.707160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-06</th>\n",
       "      <td>-1.045103</td>\n",
       "      <td>-0.116764</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2013-01-01 -1.016938  2.024969\n",
       "2013-01-02 -1.018664 -1.006544\n",
       "2013-01-03 -0.402324 -0.842240\n",
       "2013-01-04  0.003951  1.596461\n",
       "2013-01-05 -0.151427  1.707160\n",
       "2013-01-06 -1.045103 -0.116764"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selecting all rows (:) with a select column labels\n",
    "df.loc[:, [\"A\", \"B\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-01-02</th>\n",
       "      <td>-1.018664</td>\n",
       "      <td>-1.006544</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-03</th>\n",
       "      <td>-0.402324</td>\n",
       "      <td>-0.842240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-04</th>\n",
       "      <td>0.003951</td>\n",
       "      <td>1.596461</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2013-01-02 -1.018664 -1.006544\n",
       "2013-01-03 -0.402324 -0.842240\n",
       "2013-01-04  0.003951  1.596461"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# For label slicing both endpoints are included\n",
    "df.loc[\"20130102\": \"20130104\", [\"A\", \"B\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    0.003951\n",
       "B    1.596461\n",
       "C    0.158366\n",
       "D    0.528652\n",
       "Name: 2013-01-04 00:00:00, dtype: float64"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selection by position\n",
    "df.iloc[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-01-04</th>\n",
       "      <td>0.003951</td>\n",
       "      <td>1.596461</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-05</th>\n",
       "      <td>-0.151427</td>\n",
       "      <td>1.707160</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2013-01-04  0.003951  1.596461\n",
       "2013-01-05 -0.151427  1.707160"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Integer slices acts similar to Numpy/Python:\n",
    "df.iloc[3:5, 0:2] # row, column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-01-02</th>\n",
       "      <td>-1.018664</td>\n",
       "      <td>0.451620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-03</th>\n",
       "      <td>-0.402324</td>\n",
       "      <td>2.158730</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-01-05</th>\n",
       "      <td>-0.151427</td>\n",
       "      <td>-0.976849</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         C\n",
       "2013-01-02 -1.018664  0.451620\n",
       "2013-01-03 -0.402324  2.158730\n",
       "2013-01-05 -0.151427 -0.976849"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# List of integer position locations\n",
    "df.iloc[[1, 2, 4], [0, 2]]"
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
       "2013-01-02    1\n",
       "2013-01-03    2\n",
       "2013-01-04    3\n",
       "2013-01-05    4\n",
       "2013-01-06    5\n",
       "2013-01-07    6\n",
       "Freq: D, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setting\n",
    "# Setting a new column automatically aligns the data by the indexes\n",
    "s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range(\"20130102\", periods=6))\n",
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'A'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mpandas\\_libs\\tslibs\\conversion.pyx\u001b[0m in \u001b[0;36mpandas._libs.tslibs.conversion._convert_str_to_tsobject\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\tslibs\\parsing.pyx\u001b[0m in \u001b[0;36mpandas._libs.tslibs.parsing.parse_datetime_string\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Given date string not likely a datetime.",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\datetimes.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m    602\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 603\u001b[1;33m                 \u001b[0mkey\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_maybe_cast_for_get_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    604\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\datetimes.py\u001b[0m in \u001b[0;36m_maybe_cast_for_get_loc\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    630\u001b[0m         \u001b[1;31m# needed to localize naive datetimes\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 631\u001b[1;33m         \u001b[0mkey\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTimestamp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    632\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtzinfo\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\tslibs\\timestamps.pyx\u001b[0m in \u001b[0;36mpandas._libs.tslibs.timestamps.Timestamp.__new__\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\tslibs\\conversion.pyx\u001b[0m in \u001b[0;36mpandas._libs.tslibs.conversion.convert_to_tsobject\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\tslibs\\conversion.pyx\u001b[0m in \u001b[0;36mpandas._libs.tslibs.conversion._convert_str_to_tsobject\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to Timestamp",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-32-c19168976368>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ms1\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"A\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    880\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    881\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mkey_is_scalar\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 882\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    883\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    884\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mis_hashable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m_get_value\u001b[1;34m(self, label, takeable)\u001b[0m\n\u001b[0;32m    987\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    988\u001b[0m         \u001b[1;31m# Similar to Index.get_value, but we do not fall back to positional\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 989\u001b[1;33m         \u001b[0mloc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    990\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_values_for_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mloc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    991\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\datetimes.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m    603\u001b[0m                 \u001b[0mkey\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_maybe_cast_for_get_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    604\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 605\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    606\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    607\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtimedelta\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'A'"
     ]
    }
   ],
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
