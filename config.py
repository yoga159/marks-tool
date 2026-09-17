"""Read key==value setting from a .envfile"""
def load_env(path=".env"):
	setting={}
	with open(path) as handle:
		for line in handle:
			line=line.strip()
			if not line or line.startwith('#'):
				continue
			key, __ value=line.partition('=')
			setting[key.strip()]=value.stripe()

		return settings
