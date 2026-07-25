class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {res}")
        # res = 0
        # for idx, v1 in enumerate(V1):
        #     res += v1 * V2[idx]

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is : {res}")
