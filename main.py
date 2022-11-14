import csv
class BlockVote:
  def __init__(self, l_candidates):
    self.candidates = {}
    for i in range(1, l_candidates+1):
      self.candidates[i] = 0
    print(self.candidates)

  def enter_ballots(self, path):
    with open(path) as f:
      self.ballots = csv.reader(f)
      for row in self.ballots:
          self.ballot = [int(x) for x in row]
          for i in self.ballot:
            if i in list(self.candidates.keys()):
              self.candidates[i] += 1
            else:
              pass
      print(self.candidates)
  def winner(self, seats=None):
    self.sortedcandidates = sorted(self.candidates, key=self.candidates.get, reverse=True)
    print(self.sortedcandidates[0:seats])

vote = BlockVote(4)
vote.enter_ballots('ballots.csv')
vote.winner(2)