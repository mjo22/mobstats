
import softstats

if softstats.config.gpu is False:
    from .powerspectrum import powerspectrum
    from .bispectrum import bispectrum
else:
    from .cuda_powerspectrum import powerspectrum
    from .cuda_bispectrum import bispectrum

del softstats
