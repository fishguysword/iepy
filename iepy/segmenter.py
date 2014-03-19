from iepy.models import PreProcessSteps, TextSegment
from iepy.preprocess import BasePreProcessStepRunner


class SyntacticSegmenterRunner(BasePreProcessStepRunner):

    step = PreProcessSteps.segmentation

    def __init__(self, override=False):
        self.override = override

    def __call__(self, doc):
        if not doc.was_preprocess_done(PreProcessSteps.nerc) or not doc.was_preprocess_done(PreProcessSteps.sentencer):
            return
        if self.override or not doc.was_preprocess_done(self.step):
            doc.build_syntactic_segments()
            self.flag_preprocess_done(self.step)


class ContextualSegmenterRunner(BasePreProcessStepRunner):

    step = PreProcessSteps.segmentation

    def __init__(self, distance, override=False):
        self.distance = distance
        self.override = override

    def __call__(self, doc):
        if not doc.was_preprocess_done(PreProcessSteps.nerc):
            return
        if self.override or not doc.was_preprocess_done(self.step):
            doc.build_contextual_segments(self.distance)
            self.flag_preprocess_done(self.step)
