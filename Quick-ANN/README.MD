TF-install

conda update -n base conda
conda create -n tf-metal-p12.2 python=3.12.2
conda activate tf-metal-p12.2


python -m pip install -U pip
pip install tensorflow
pip install "pandas[performance, plot, output-formatting, computation, feather, gcp]"


	| conda install notebook -y
	| conda install -c conda-forge jupyterthemes
	| jt -l
	| jt -t oceans16

pwd | xargs jupyter notebook --notebook-dir=


