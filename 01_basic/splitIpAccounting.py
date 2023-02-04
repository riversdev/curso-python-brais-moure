re = ''

def splitIpAccounting(self, result):
    self.log.DEBUG('Processing Ip Accounting data')
    self.log.DEBUG('Set Ip Accounting validation')

    code = ''
    counter = 0

    for row in result.split('\n'):
        if 'Accounting' in row and counter >= 2:
            return 'Ip Accounting without record'

        if ((not re.search('[0-9]', row) or 'Accounting' in row) and counter > 2):
            break

        code += '<tr class="headers format">' if counter == 0 else '<tr>'

        for col in row.split(' '):
            code += '' if ' ' in col else f'<td>{col}</td>'
        
        code += '</tr>'
        counter += 1
    
    self.log.DEBUG(f'{counter} records processed in Ip Accounting data')

    return code