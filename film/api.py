import requests
import random


from film.models import FilmSerie

def get_movies():
    api_key = '9ad676507c500022c8426990e4df79ee'
    for i in range(2,200):
        url = f'https://api.themoviedb.org/3/movie/{i}?api_key={api_key}'
        response = requests.get(url)
        data = response.json()
    return data

# def get_genre_names(genres):
#     genre_names = []
#     for genre in genres:
#         genre_names.append(genre['name'])
#     return genre_names

def add_movies():
    api_key = '9ad676507c500022c8426990e4df79ee'
    number = random.randint(1, 10000)
    
    lists = [
 17711,
 328111,
 8698,
 93456,
 602,
 330,
 953,
 9693,
 36657,
 8909,
 9802,
 950,
 1824,
 2976,
 11026,
 332,
 75656,
 38365,
 594,
 15189,
 11678,
 6538,
 10555,
 1125,
 4551,
 612,
 9567,
 37821,
 203801,
 2539,
 9297,
 3172,
 6520,
 1439,
 37958,
 2026,
 7450,
 11375,
 9425,
 25769,
 23685,
 11866,
 9741,
 211672,
 23629,
 8688,
 10153,
 153518,
 8676,
 20829,
 4349,
 9718,
 10808,
 197,
 25,
 35,
 11086,
 10477,
 1997,
 6947,
 3050,
 2675,
 809,
 920,
 4806,
 7451,
 228165,
 3595,
 16869,
 879,
 1573,
 9257,
 1903,
 9697,
 395,
 23398,
 10590,
 117263,
 200,
 44943,
 587,
 10395,
 57212,
 152760,
 2756,
 33909,
 49017,
 9882,
 2270,
 978,
 44564,
 3132,
 8814,
 8427,
 52520,
 80585,
 10592,
 49021,
 11535,
 10550,
 11258,
 12610,
 59981,
 201088,
 5137,
 3093,
 107846,
 188207,
 4614,
 24021,
 11371,
 20352,
 11517,
 214756,
 26428,
 9824,
 48988,
 9008,
 300673,
 12113,
 38778,
 72331,
 1844,
 846,
 9703,
 857,
 136797,
 3981,
 425,
 6171,
 72976,
 603,
 568,
 9021,
 82695,
 9489,
 12133,
 9342,
 41733,
 227306,
 5551,
 9350,
 9208,
 4244,
 1852,
 11820,
 76493,
 345,
 196867,
 256591,
 59962,
 36648,
 1880,
 9440,
 71679,
 10483,
 11412,
 11983,
 6795,
 550,
 11170,
 9292,
 10783,
 100241,
 257,
 9947,
 189,
 12618,
 253412,
 1427,
 818,
 16577,
 329,
 12160,
 9331,
 300168,
 9072,
 3536,
 9087,
 12177,
 12138,
 273248,
 9955,
 50359,
 1271,
 693,
 14306,
 497,
 11199,
 9982,
 210577,
 2501,
 710,
 2275,
 37165,
 9837,
 10708,
 136400,
 10992,
 9654,
 2642,
 8916,
 19899,
 2119,
 9641,
 294254,
 38167,
 5994,
 39514,
 9563,
 547,
 1538,
 9334,
 11128,
 75780,
 8914,
 13576,
 39538,
 10628,
 14836,
 8645,
 9509,
 10067,
 9384,
 9279,
 1487,
 9422,
 77174,
 4824,
 9620,
 9302,
 10199,
 10771,
 3512,
 137094,
 274479,
 267860,
 8078,
 7485,
 170687,
 6435,
 137106,
 10040,
 6278,
 82682,
 17610,
 22954,
 16995,
 16558,
 9849,
 5820,
 16866,
 201,
 11775,
 87825,
 12201,
 11015,
 9932,
 13389,
 8838,
 17332,
 4958,
 786,
 9513,
 11679,
 38321,
 14411,
 8413,
 10052,
 9676,
 9664,
 2100,
 10384,
 137321,
 123553,
 11260,
 9009,
 11374,
 2309,
 8285,
 210860,
 2312,
 9839,
 381902,
 13922,
 293660,
 9713,
 190859,
 257445,
 9007,
 889,
 1370,
 4942,
 347969,
 24438,
 116741,
 35791,
 72431,
 1813,
 87428,
 8840,
 10589,
 71676,
 1722,
 10022,
 11358,
 13,
 6477,
 1597,
 10530,
 1924,
 9327,
 8488,
 10603,
 8273,
 109424,
 35056,
 8839,
 156022,
 7303,
 8963,
 1402,
 9315,
 8984,
 795,
 24,
 11353,
 393,
 9618,
 9374,
 8584,
 2320,
 58224,
 1729,
 175574,
 8077,
 8818,
 8195,
 10586,
 116149,
 80035,
 10632,
 12117,
 1792,
 13260,
 72197,
 3580,
 12123,
 9566,
 9833,
 4517,
 8202,
 16072,
 34314,
 19724,
 145220,
 14623,
 42297,
 2841,
 802,
 10375,
 36586,
 11321,
 70074,
 242,
 9621,
 1819,
 8536,
 8046,
 1717,
 479,
 9444,
 824,
 11456,
 261023,
 3683,
 22803,
 285923,
 39437,
 1950,
 640,
 97630,
 9767,
 11631,
 32856,
 6519,
 8741,
 49520,
 1850,
 524,
 26389,
 11817,
 2123,
 9907,
 9969,
 18239,
 808,
 38050,
 8367,
 9390,
 72105,
 2898,
 10312,
 109443,
 2022,
 37686,
 462,
 9919,
 187017,
 628,
 10201,
 302699,
 9441,
 274167,
 224141,
 388,
 2112,
 10329,
 74465,
 13811,
 6877,
 10320,
 50646,
 8920,
 13673,
 60308,
 6950,
 225574,
 13836,
 752,
 6038,
 9975,
 11451,
 12103,
 60304,
 2251,
 46529,
 231,
 300671,
 228326,
 9754,
 66,
 4421,
 2649,
 588,
 10393,
 71552,
 9631,
 216282,
 306,
 928,
 205587,
 6623,
 1577,
 9801,
 2116,
 9624,
 14199,
 1907,
 4599,
 22832,
 10390,
 9879,
 38579,
 44603,
 11892,
 9691,
 1248,
 12220,
 72710,
 1255,
 72710,
 1255,
 10782,
 9573,
 4959,
 10061,
 10386,
 421,
 316152,
 11615,
 13498,
 241554,
 2252,
 11968,
 10047,
 38319,
 69668,
 9770,
 11212,
 10533,
 38363,
 9923,
 11863,
 18501,
 109491,
 9275,]
    
    for list in lists:
    
        url = f'https://api.themoviedb.org/3/movie/{list}?api_key={api_key}'
        response = requests.get(url)
        data = response.json()
        if "title" not in data:
            print(0)
            continue
        
        if data.get('poster_path') is None:
            print(0)
            continue
        
        try :


            genre_names =[genre["name"] for genre in data.get("genres", [])]
            genre_name = ", ".join(genre_names)

            FilmSerie.objects.update_or_create(
                id=list,
                defaults={ 
                    'title': data['title'], 
                    'poster_path': data['poster_path'],
                    'id': data['id'], 
                    'description': data['overview'],
                    'datef': data['release_date'], 
                    'langue': data['original_language'],
                    'genre': genre_name, # add genre name
                }
            )
        except KeyError:
            continue
            


def get_movies_details(movie_id):
    api_key = '9ad676507c500022c8426990e4df79ee'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data