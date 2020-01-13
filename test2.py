import pymiere

qe = pymiere.objects.qe

# print(qe)
# qe.inspect()
qe.project.inspect()
video_effects = qe.project.getVideoEffectList()
print([v for v in video_effects])
# qe.source