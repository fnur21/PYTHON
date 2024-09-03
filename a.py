import math

# 1. Adım: Noktaların Tanımlanması
# 2D uzayındaki noktalarımızı tuple'lar olarak tanımlıyoruz.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# 2. Adım: Öklid Mesafesi Fonksiyonu
# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon.
def euclideanDistance(point1, point2):
    # (x2 - x1)^2 + (y2 - y1)^2 formülüne göre mesafe hesaplanır
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Adım: Mesafelerin Hesaplanması
# Tüm noktalar arasındaki mesafeleri hesaplayıp bir listeye ekliyoruz.
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # İki nokta arasındaki mesafeyi hesapla ve distances listesine ekle
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Adım: Minimum Mesafenin Bulunması
# distances listesinden minimum mesafeyi bulup yazdırıyoruz.
min_distance = min(distances)
print("Minimum distance:", min_distance)
