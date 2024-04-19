import sys
import hashlib

def calcular_geohash(latitude, longitude):
    coordenadas_str = "{:.12f},{:.12f}".format(latitude, longitude)
    hash_object = hashlib.md5(coordenadas_str.encode())
    return hash_object.hexdigest()[:10]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python geohashing.py <latitude> <longitude>")
        sys.exit(1)

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        geohash = calcular_geohash(latitude, longitude)
        print("Geohash:", geohash)

    except Exception as e:
        print("Ocorreu um erro:", e)
