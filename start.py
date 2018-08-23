def func(self):
	import sh
	for url in self.settings.URLS.split("|"):
		self.info(self.rid, url)
		s=sh.siege("-c2", "--time=5S", url, _iter=True, _err_to_out=True)
		self.debug(self.rid, str(s.__dict__))
		self.info(self.rid, str(s.ran))
		self.debug(self.rid, str(s))
		for line in s:
			if "transaction" in line.lower():
				self.info(self.rid, str(line))
	return "FINISHED"