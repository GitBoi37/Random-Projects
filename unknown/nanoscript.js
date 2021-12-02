//======================== roll Martingale ====================
var config = {
    baseBet: { label: 'base bet', value: currency.minAmount, type: 'number' },
    payout: { label: 'payout', value: 2, type: 'number' },
    onLoseTitle: { label: 'On Lose', type: 'title' },
    onLoss: { 
      label: '', value: 'reset', type: 'radio',
      options: [
        { value: 'reset', label: 'Return to base bet' },
        { value: 'increase', label: 'Increase bet by (loss multiplier)' }
      ]
    },
    lossMultiplier: { label: 'loss multiplier', value: 2, type: 'number' },
    onWinTitle: { label: 'On Win', type: 'title' },
    onWin: { 
      label: '', value: 'reset', type: 'radio',
      options: [
        { value: 'reset', label: 'Return to base bet' },
        { value: 'increase', label: 'Increase bet by (win multiplier)' }
      ]
    },
    winMultiplier: { label: 'win multiplier', value: 2, type: 'number' },
  }
  
  function main () {
    var currentBet = config.baseBet.value
    engine.on('GAME_STARTING', function () {
      engine.bet(currentBet, config.payout.value)
    })
  
    engine.on('GAME_ENDED', function (data) {
      // we won...
      if (data.profitAmount > 0) {
        if (config.onWin.value === 'reset') {
          currentBet = config.baseBet.value;
        } else {
          currentBet *= config.winMultiplier.value;
        }
        //log.success('We won, so next bet will be ' + currentBet + ' ' + currency.currencyName)
      } else {
        if (config.onLoss.value === 'reset') {
          currentBet = config.baseBet.value;
        } else {
          currentBet *= config.lossMultiplier.value;
        }
        //log.error('We lost, so next bet will be ' + currentBet + ' ' + currency.currencyName)
      }
    })
  }