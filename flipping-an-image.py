class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()

        for j in range(len(image)):
            for i in range(len(image[j])):
                if image[j][i] == 1:
                    image[j][i] = 0
                else:
                    image[j][i] = 1

        return image
