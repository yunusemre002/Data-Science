import time
import logging

from zemberek import (
    TurkishSentenceNormalizer,
    TurkishMorphology,
)

logger = logging.getLogger(__name__)

examples = ["poscihazı hep bozuk nedense",
            "hızlı servis güleryüzlü garsonlar",
            "yemekelr süpeerdi ama servis yavş dahası ilgelimiyor.",
            "leeş"]

morphology = TurkishMorphology.create_with_defaults()

# SENTENCE NORMALIZATION
# start = time.time()
normalizer = TurkishSentenceNormalizer(morphology)
# logger.info(f"Normalization instance created in: {time.time() - start} s")

# start = time.time()
for example in examples:
    print(example)
    print(normalizer.normalize(example), "\n")
# logger.info(f"Sentences normalized in: {time.time() - start} s")



# # SENTENCE BOUNDARY DETECTION
# start = time.time()
# extractor = TurkishSentenceExtractor()
# print("Extractor instance created in: ", time.time() - start, " s")
#
# text = "İnsanoğlu aslında ne para ne sevgi ne kariyer ne şöhret ne de çevre ile sonsuza dek mutlu olabilecek bir " \
#        "yapıya sahiptir. Dış kaynaklardan gelebilecek bu mutluluklar sadece belirli bir zaman için insanı mutlu " \
#        "kılıyor. Kişi bu kaynakları elde ettiği zaman belirli bir dönem için kendini iyi hissediyor, ancak alışma " \
#        "dönemine girdiği andan itibaren bu iyilik hali hızla tükeniyor. Mutlu olma sanatının özü bu değildir. Gerçek " \
#        "mutluluk, kişinin her türlü olaya ve duruma karşı kendini pozitif tutarak mutlu hissedebilmesi halidir. Bu " \
#        "davranış şeklini edinen insan, zor günlerde güçlü, mutlu günlerde zevk alan biri olur ve mutluluğu kalıcı " \
#        "kılar. "
#
# start = time.time()
# sentences = extractor.from_paragraph(text)
# print(f"Sentences separated in {time.time() - start}s")
#
# for sentence in sentences:
#     print(sentence)
# print("\n")

