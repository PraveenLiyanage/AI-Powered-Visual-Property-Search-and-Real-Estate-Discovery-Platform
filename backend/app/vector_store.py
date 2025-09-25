import faiss
import numpy as np
import json
import os

class FaissStore:
    def __init__(self, dim=512, index_path="faiss.index", mapping_path="id_map.json"):
        self.dim = dim
        self.index_path = index_path
        self.mapping_path = mapping_path

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self._load_map()
        else:
            self.index = faiss.IndexFlatIP(dim)
            self.id_map = []

    def _load_map(self):
        with open(self.mapping_path, 'r') as f:
            self.id_map = json.load(f)

    def _save_map(self):
        with open(self.mapping_path, 'w') as f:
            json.dump(self.id_map, f)

    def add(self, vec: np.ndarray, property_id: int):
        vec = np.asarray([vec]).astype('float32')
        self.index.add(vec)
        self.id_map.append(property_id)
        self._save_map()
        faiss.write_index(self.index, self.index_path)

    def search(self, vec: np.ndarray, top_k=5):
        vec = np.asarray([vec]).astype('float32')
        scores, idxs = self.index.search(vec, top_k)
        results = []
        for score, idx in zip(scores[0], idxs[0]):
            if idx == -1:
                continue
            property_id = self.id_map[idx]
            results.append({'property_id': property_id, 'score': float(score)})
        return results
