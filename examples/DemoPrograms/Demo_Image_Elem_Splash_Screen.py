import simplegui as sg

"""
    Demo - Splash Screen
    
    Displays a PNG image with transparent areas as see-through on the center
    of the screen for a set amount of time.
    
    Copyright 2020 PySimpleGUI.org
"""

image = b'iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAACXBIWXMAABcRAAAXEQHKJvM/AAAgAElEQVR4nOzdd3gUVdsG8Hu2pfdCCJCA0qQIiIj0pqJ0EBRUioq919eGouBnQ8XepQsCoih2SkBa6L0TQgrpvW+Z+f6gZZOd3dnsbtrcP6693peZs+c8s8hy58ycGUGSJBARERGRemjqugAiIiIiql0MgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDIMgEREREQqwwBIREREpDK6ui6AiOjUudzA5KyCdhsPJnUC0PnI2azmJ1Nz/C/slnq2b5YbFRpwMjYy6EC3K6P2XRUTnuSl14l1WbOsirO+sBTGwJjUBKUHIi5sNSJoaDoEfQYMzVOhCzHXaY1EpHqCJEl1XQMRqVBuUZnvr9uO9/5r16lJZzMLBpUbzc0AGJS8tVlYwL6+nWK+v++Wa34NC/Qt8nStDlmKdchbfR0KN05GxZnBEMuiAfgBECq3AlAAXVg6dKGbEHTDXwgeGgdtSCEELb+IiahWMQASUa3KyCv2Wxp3aNrK/448VFJu6uhKX77e+hPj+3Z4a9KgTgujQvzrZkYwa35v5Cx/CZbCW+D8ZTXn4NvlZwT2+w4hY/ZB480vZCKqFQyARFQryipMhs/X7Bq1avPR2aUVprawnh1zhdgiIvC3h0f2eOLma1ufdVOfjplzfHH2uZdQfvIpQPJ1sbdy6MLXIWLqXAQNiYM2kKeIicijGACJyOOOJWc3eWne+o/OpOfdCg9de6zTao7PuKP/baN6tTvgif6tlO4PQdrc71B+cqybezZB33QNQse+hvBJB92XkYmIrDEAEpFHffxL/PB5/+z7HEBMLQyX8+pdA0aN7d1+q8dGKNwYieRX/gCk7h4bAzDDt+sXiLz7Lfh1T/PgOESkUgyAROQROYVlPv/77t+n95xKe1mS4FNb4+p12nMv3N7ntnF9rtri9s4LNzRF6uwVECv6uL1vWwTtGYSMeRVNHlgOja+xVsYk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IAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqAwCIAAAAIDKIAACAAAAqMz/B7LJu0uHjbFxAAAAAElFTkSuQmCC'


FILENAME = r'yourfile.png'          # if you want to use a file instead of data, then use this in Image Element
DISPLAY_TIME_MILLISECONDS = 4000

sg.Window('Window Title', [[sg.Image(data=image)]], transparent_color=sg.theme_background_color(), no_titlebar=True, keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)
